import sys
import csv
import random
import numpy as np

class MyParser:
    def __init__(self, description=None):
        self.description = description
        self.arg_dict = {}

    def _short_usage(self):
        short_usage = "usage: " + sys.argv[0] + " [-h]"
        for k,v in self.arg_dict.items():
            short_usage += " " + k + " " + k.upper()
        return short_usage

    def _long_usage(self):
        long_usage = f"{self._short_usage()}\n\n{self.description}\n\n"\
                     "required arguments:\n"
        for k,v in self.arg_dict.items():
            long_usage +=  f"  {k} {k.upper()}    {v['help']}\n"
        long_usage += f"\noptional arguments:\n  -h                   "\
                      "show this help message and exit"
        return long_usage

    def _error(self, string=None):
        err = f"{self._short_usage()}\n{sys.argv[0]}: error: {string}"
        print(err)
        exit(1)

    def add_argument(self, arg_name, type, action='store', help=None):
        self.arg_dict.update({arg_name: {'type': type,
                                         'action': action,
                                         'help': help}})

    def parse_args(self):
        cml = sys.argv[1:]

        if "-h" in cml:
            print(self._long_usage())
            exit(0)

        cml = [x.split('=') for x in cml]

        for x in cml:
            k = x[0]
            attr = self.arg_dict.get(k)

            if attr is None:
                self._error(f"unrecognized arguments: {x[0]}={x[1:]}")

            if attr['action'] is 'store':
                if len(x) < 2:
                    self._error(f"missing {self.arg_dict[k]['type'].__name__}"
                                f" arguments to: {x[0]}")
                v = '='.join(x[1:])
                if not isinstance(v, self.arg_dict[k]['type']):
                    try:
                        v = self.arg_dict[k]['type'](v)
                    except ValueError:
                        self._error(f"argument {k}: invalid"
                                    f" {self.arg_dict[k]['type'].__name__}"
                                    f" value: '{v}'")
            self.arg_dict[k].update({'arg':v})

        return {k:v['arg'] for k,v in self.arg_dict.items()}



class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids 
        self.centroids = [] # values of the centroids

    def _init_random_centroids(self, X):
        #Randomly pick vectors from the given matrix in a set so they are unique
        centroid_set = set()
        while len(centroid_set) != self.ncentroid:
            centroid_set.add(tuple(np.copy(X[random.randint(0, len(X) - 1)])))

        return np.array([list(f) for f in centroid_set])

    def _label_vectors(self, X, centroids, labels):
        if len(X) != len(labels):
            exit(1)

        # For each vectors, calculate its distance with each centroids and
        # label the vector with its closest centroid, thus creating clusters
        for k, vec in enumerate(X):
            shortest_dist, centroid_idx = None, None
            for j, centroid in enumerate(centroids):
                dist = np.linalg.norm(vec[:3] - centroid) # Euclidian dist
                if shortest_dist is None:
                    shortest_dist, centroid_idx = dist, 0
                if dist < shortest_dist:
                    shortest_dist, centroid_idx = dist, j
            labels[k] = centroid_idx # label the vector

    def fit(self, X):
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          None.
        Raises:
        -------
          This function should not raise any Exception.
        """

        if self.ncentroid > X.shape[0]:
            return None

        centroid_set = self._init_random_centroids(X)

        # label column so we can create clusters then
        labels = np.zeros((X.shape[0], 1))

        for i in range(0, self.max_iter):
    
            self._label_vectors(X, centroid_set, labels)

            # Calculate the mean vector of each cluster and replace it in the
            # centroid set
            same_val = 0
            for j in range(0, self.ncentroid):
                cluster = X[labels[..., 0] == j]
                mean_vec = np.array([np.mean(cluster[...,0]),
                                     np.mean(cluster[...,1]),
                                     np.mean(cluster[...,2])])
                if np.array_equal(mean_vec, centroid_set[j]):
                    same_val += 1
                centroid_set[j] = mean_vec

            # Stop calculation if centroids won't change anymore
            if same_val == self.ncentroid:
                break

        self.centroids = centroid_set.copy()

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
          X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
          the prediction as a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
          This function should not raise any Exception.
        """
        # With the help of the trained centroids with can give back a label
        # array corresponding to the given X set.
        labels = np.zeros((X.shape[0], 1))
        self._label_vectors(X, self.centroids, labels)
        return labels

    def disp_individuals_nb(self, X, labels):
        if len(X) != len(labels):
            return None
    
        ncentroids = len(np.unique(labels))
        centroids = self.centroids

        if ncentroids != len(centroids):
            return None
    
        # Display the number of individuals associated to each centroids
        for j in range(0, ncentroids):
            print(f"centroid {j} {centroids[j]} individuals number: "
                  f"{len(X[labels[..., 0] == j])}")

    def disp_regions(self):
        ncentroids = self.ncentroid
        centroids = self.centroids

        if ncentroids != len(centroids) or ncentroids != 4:
            return None
    
        # display the coordinates of the different centroids and the
        # associated region (for the case ncentroid=4)
        height, weight, bd = 0, 1, 2
        print("Centroids and its associated regions:")
        maxx = np.argmax(centroids, axis=0)
        print(f"\tbelt citizens: {centroids[maxx[height]]}")
    
        # hide belt citizens to facilitate next operations
        mask = (centroids != centroids[maxx[height]]).all(-1)
        centroids = centroids[mask]
    
        minn = np.argmin(centroids, axis=0)
        maxx = np.argmax(centroids, axis=0)
    
        # find earthians. They can't be the tallest nor the lightest
        mask = (centroids != centroids[maxx[height]]).all(-1)
        mask2 = (centroids != centroids[minn[weight]]).all(-1)
        # logical AND to join the masks in the purpose to isolate earthians
        earthians = centroids[mask == mask2]
    
        # if we didn't succeeded isolation, there is a lack of data for
        # the next presumptions so we exit
        if len(earthians) != 1:
            print(f"{sys.argv[0]}: err: can't resolve citizens origin with"
                  " this fit, run again.")
            return None
    
        mask_martians = centroids[:,height] > earthians.ravel()[height]
        martians = centroids[mask_martians]
    
        mask_venusians = centroids[:,weight] < earthians.ravel()[weight]
        venusians = centroids[mask_venusians]
    
        if len(martians) == 2:
            mask_martians = (martians != venusians)
            martians = martians[mask_martians]
        elif len(venusians) == 2:
            mask_venusians = (venusians != martians)
            venusians = venusians[mask_venusians]
    
        print(f"\tearth citizens: {earthians.ravel()}\n"
              f"\tmars citizens: {martians.ravel()}\n"
              f"\tvenus citizens: {venusians.ravel()}")


parser = MyParser(description = 'minimalist K-mean algorithm')
parser.add_argument('filepath', type=str, help='dataset to process')
parser.add_argument('ncentroid', type=int, help='number of centroids')
parser.add_argument('max_iter', type=int, help='maximum number of iterations')
args = parser.parse_args()

arr = None

try:
    arr = np.genfromtxt(args['filepath'],
                        delimiter=",",
                        skip_header=True,
                        usecols=(1,2,3))
except OSError:
    print(f"{sys.argv[0]}: err: oops can't open '{args['filepath']}'")
    exit(1)
except ValueError as err:
    print(f"{sys.argv[0]}: err: {err}")
    exit(1)

kmeans = KmeansClustering(args['max_iter'], args['ncentroid'])

kmeans.fit(arr)
labels = kmeans.predict(arr)
kmeans.disp_individuals_nb(arr, labels)
kmeans.disp_regions()

new_set = arr[11::2,:]

labels = kmeans.predict(new_set)
kmeans.disp_individuals_nb(new_set, labels)

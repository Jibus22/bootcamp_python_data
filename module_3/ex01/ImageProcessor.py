import matplotlib.pyplot as plt
import numpy as np

class ImageProcessor:
    def load(self, path):
        img = None
        try:
            img = plt.imread(path)
            print(f"Loading image of dimensions {img.shape[0]}x{img.shape[1]}")
        except Exception as err:
            print(f"{err}")
        return img

    def display(self, array):
        if not isinstance(array, np.ndarray):
            print(f"array is not valid")
            return None
        plt.axis("off")
        try:
            plt.imshow(array)
            plt.show()
        except Exception as err:
            print(f"{err}")

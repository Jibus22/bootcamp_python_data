from math import sqrt

class TinyStatistician:
    def __init__(self):
        pass

    def mean(self, x):
        """ computes the mean of a given non-empty list or array x
            @x:       list(x) list to compute
            @return   the mean as a float, otherwise None if x is
                      an empty list or array
        """
        xlen = len(x)
        if xlen < 2:
            return None

        return sum(val for val in x) / xlen

    def median(self, x):
        """ computes the median of a given non-empty list or array x
            @x:       list(x) list to compute
            @return   the median as a float, otherwise None if x is
                      an empty list or array
        """
        xlen = len(x)
        if xlen < 2:
            return None

        x.sort()
        if ((xlen % 2) == 0):
            idx1 = (xlen // 2) - 1
            idx2 = idx1 + 1
            return (x[idx1] + x[idx2]) / 2
        else:
            idx = ((xlen + 1) // 2) - 1
            return x[idx]
        pass

    def quartile(self, x):
        """ computes the 1st and 3rd quartiles of a given non-empty array x
            @x:       list(x) list to compute
            @return   the quartile as a float, otherwise None if x
                      is an empty list or array.
        """
        xlen = len(x)
        if xlen < 3:
            return None
        x.sort()
        med = self.median(x)
        for i in range(len(x)):
            if x[i] > med:
                med = i - 1 # find index of median value
                break
        if xlen % 2 is 0:
            q1 = self.median(x[:med + 1])
            q3 = self.median(x[med + 1:])
        else:
            q1 = self.median(x[:med])
            q3 = self.median(x[med + 1:])
        return [q1, q3]


    def var(self, x):
        """ computes the variance of a given non-empty list or array x
            @x:       list(x) list to compute
            @return   the variance as a float, otherwise None if x
                      is an empty list or array.
        """
        xlen = len(x)
        if xlen < 2:
            return None
        x.sort()
        mean = self.mean(x)
        return sum(pow((val - mean), 2) for val in x) / xlen

    def std(self, x):
        """ computes the standard deviation of a given non-empty list or array x
            @x:       list(x) list to compute
            @return   the variance as a float, otherwise None if x
                      is an empty list or array.
        """
        xlen = len(x)
        if xlen < 2:
            return None
        x.sort()
        return sqrt(self.var(x))

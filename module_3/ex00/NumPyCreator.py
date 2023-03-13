import numpy as np

class NumPyCreator:
    def __init__(self):
        pass

    def _shape_sanitize(self, struct, ttype):
        if not isinstance(struct, ttype):
            return False
        if len(struct) is 0:
            return True
        if type(struct[0]) is ttype:
            elem_len = len(struct[0])
            for x in struct:
                if not isinstance(x, ttype) or not len(x) is elem_len:
                    return False
        return True

    def _check_shape_value(self, shape):
        return (not isinstance(shape, tuple) or len(shape) < 1 or len(shape) > 2\
                or not all([(isinstance(x, int) and x >= 0) for x in shape]))

    def from_list(self, lst):
        """
        takes a list or nested lists and returns its corresponding Numpy array.
        """
        if not self._shape_sanitize(lst, list):
            return None
        return np.array(lst)

    def from_tuple(self, tpl):
        """
        takes a tuple or nested tuple and returns its corresponding Numpy array.
        """
        if not self._shape_sanitize(tpl, tuple):
            return None
        return np.array(tpl)

    def from_iterable(self, itr):
        """
        takes an iterable and returns an array which contains all its elements.
        """
        if not hasattr(itr, '__iter__'):
            return None
        if not self._shape_sanitize(itr, range):
            return None
        return np.array(itr)

    def from_shape(self, shape, value=0):
        """
        returns an array filled with the same value. The first argument is a
        tuple which specifies the shape of the array, and the second argument
        specifies the value of the elements.
        """
        if self._check_shape_value(shape):
            return None
        if not isinstance(value, int) or value < 0:
            return None
        return np.full(shape, value)

    def random(self, shape):
        """
        returns an array filled with random values.
        It takes as an argument a tuple which specifies the shape of the array.
        """
        if self._check_shape_value(shape):
            return None
        return np.random.random(shape)

    def identity(self, n):
        """
        returns an array representing the identity matrix of size n.
        """
        if not isinstance(n, int) or n < 0:
            return None
        return np.identity(n)

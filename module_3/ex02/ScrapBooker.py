import numpy as np

class ScrapBooker:

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
          array: numpy.ndarray
          dim: tuple of 2 integers.
          position: tuple of 2 integers.
        Return:
        -------
          new_arr: the cropped numpy.ndarray.
          None (if combinaison of parameters not compatible).
        Raise:
        ------
          This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple)\
                or not isinstance(position, tuple) or len(dim) is not 2\
                or len(position) is not 2:
            return None
        if not all([isinstance(x, int) and x >= 0 for x in dim])\
                or not all([isinstance(x, int) and x >= 0 for x in position]):
            return None
        if position[0] + dim[0] > array.shape[0]\
                or position[1] + dim[1] > array.shape[1]:
            return None
        return array[position[0]:position[0] + dim[0],\
                     position[1]:position[1] + dim[1]]

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis
        (0: Horizontal, 1: Vertical)
        Args:
        -----
          array: numpy.ndarray.
          n: non null positive integer lower than the number of row/column
          of the array
             (depending of axis value).
          axis: positive non null integer.
        Return:
        -------
          new_arr: thined numpy.ndarray.
          None (if combinaison of parameters not compatible).
        Raise:
        ------
          This function should not raise any Exception.
        """
        if not isinstance(n, int) or not isinstance(axis, int)\
                or not isinstance(array, np.ndarray):
            return None
        if n < 1 or (axis is not 0 and axis is not 1):
            return None
        axis = not axis
        if n > array.shape[axis]:
            return None
        index_to_del = [x for x in range(n - 1, array.shape[axis], n)]
        return np.delete(array, index_to_del, axis)

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
          array: numpy.ndarray.
          n: positive non null integer.
          axis: integer of value 0 or 1.
        Return:
        -------
          new_arr: juxtaposed numpy.ndarray.
          None (combinaison of parameters not compatible).
        Raises:
        -------
          This function should not raise any Exception.
        """
        if not isinstance(n, int) or not isinstance(axis, int)\
                or not isinstance(array, np.ndarray):
            return None
        if n < 1 or (axis is not 0 and axis is not 1):
            return None
        new_arr = array
        for i in range(n - 1):
            new_arr = np.concatenate((new_arr, array), axis)
        return new_arr

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
          array: numpy.ndarray.
          dim: tuple of 2 integers.
        Return:
        -------
          new_arr: mosaic numpy.ndarray.
          None (combinaison of parameters not compatible).
        Raises:
        -------
          This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) or not isinstance(dim, tuple)\
                or len(dim) is not 2\
                or not all([isinstance(x, int) and x >= 0 for x in dim]):
            return None
        mosaic = self.juxtapose(array, dim[1], 1)
        mosaic = self.juxtapose(mosaic, dim[0], 0)
        return mosaic

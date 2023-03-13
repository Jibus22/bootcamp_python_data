import numpy as np

class ColorFilter:
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        invert_filtered = array.copy()
        invert_filtered[..., :3] = 1.0 - invert_filtered[..., :3]
        return invert_filtered

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        blue_filtered = np.zeros(array.shape)
        blue_filtered[...,2:] = array[...,2:]
        return blue_filtered

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        green_filtered = array.copy()
        green_filtered[..., [0,2]] *=  0
        return green_filtered

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        red_filtered = array.copy() - self.to_green(array) - self.to_blue(array)
        # If there is alpha channel, get it unchanged back:
        red_filtered[..., 3:] = array[..., 3:]
        return red_filtered

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
            celluloid filter is also known as cel-shading or toon-shading.
        Args: -----
            array: numpy.ndarray corresponding to the image.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        # Algo: get 5 values which will be taken by each channel of a pixel
        #       according to its position in this scale.

        cel_shaded = array.copy()
        # Get shades, linearly spaced
        shades = np.linspace(array.min(), array.max(), 5)

        lower_shade = shades[0]
        # Loop thru shades to detect and replace each channel in the 3D matrice
        # which is between the lower and the upper shade
        for upper_shade in shades[1:]:
            # Get the boolean matrice as a mask
            indexes = (cel_shaded > lower_shade) & (cel_shaded < upper_shade)
            cel_shaded[indexes] = lower_shade
            lower_shade = upper_shade
        return cel_shaded

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = ’mean’/’m’: performs the mean of RBG channels.
        For filter = ’weight’/’w’: performs a weighted mean of RBG channels.
        Args:
        -----
            array: numpy.ndarray corresponding to the image.
            filter: string with accepted values in [’m’,’mean’,’w’,’weight’]
            weights: [kwargs] list of 3 floats where the sum equals to 1,
                     corresponding to the weights of each RBG channels.
        Return:
        -------
            array: numpy.ndarray corresponding to the transformed image.
            None: otherwise.
        Raises:
        -------
            This function should not raise any Exception.
        """
        # Algo: To get a grey, all channels must be equal (R=G=B). The mean
        #       filter just calculate the mean of the 3 channels then set
        #       them to the result value.
        #       The weighted filter applies the weight to each channels before
        #       summing then set them to the result value.

        gsc_img = array.copy()

        if filter in ["mean", "m"]:
            gsc_img[..., :3] = np.sum(gsc_img[..., :3],
                                      axis=-1,
                                      keepdims=True) / 3.0
        elif filter in ["weight", "w"]:
            if len(kwargs) is not 1:
                return None

            weights = list(kwargs.values())[0]
            if not isinstance(weights, list) or len(weights) is not 3\
                    or not all(isinstance(x, float) for x in weights):\
                return None

            weights = np.array(weights)
            if np.sum(weights * 10).astype(int) != 10:
                return None

            gsc_img[..., :3] = np.sum(gsc_img[..., :3] * weights,
                                      axis=-1,
                                      keepdims=True)
        else:
            return None

        return gsc_img

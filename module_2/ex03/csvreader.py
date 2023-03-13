class CsvReader():
    def __init__(self, filename=None, sep=",", header=False,
                 skip_top=0, skip_bottom=0):
        if (not isinstance(filename, str) and filename is not None):
            raise Exception("TypeError: filename isn't a string")
        if not isinstance(sep, str) or not isinstance(header, bool)\
                or not isinstance(skip_top, int)\
                or not isinstance(skip_bottom, int):
            raise Exception("TypeError: wrong type on sep, header, skip_top or"
                            "skip_bottom")
        self.filename = filename
        self.sep = sep
        self.header = header
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        self._file = None
        try:
            self._file = open(self.filename)
        except FileNotFoundError:
            return None
        self.firstline = self._file.readline()
        self.firstline = [x.strip() for x in self.firstline.split(self.sep)]
        self._col_nb = len(self.firstline)

        self.data = self._file.readlines()

        self.data = [x.split(self.sep) for x in self.data]
        new_matrix = []
        for i, x in enumerate(self.data):
            new_row = []
            for y in x:
                value = y.strip()
                if value is "":
                    raise Exception(f"Bad CSV formating: line {i+1}")
                    # return None
                new_row.append(value)
            if len(new_row) is not self._col_nb:
                raise Exception(f"Bad CSV formating: line {i+1}")
                # return None
            new_matrix.append(new_row)

        self._rows_nb = len(new_matrix)
        if self._rows_nb < self.skip_top or self._rows_nb < self.skip_bottom:
            raise Exception(f"skip_[top/bottom] argument to high for the file")
            # return None

        self.data = new_matrix[self.skip_top:(self._rows_nb - self.skip_bottom)]

        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self._file is not None:
            self._file.close()
        return True

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
            nested list (list(list, list, ...)) representing the data.
        """
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        if self.header is False:
            return None
        else:
            return self.firstline

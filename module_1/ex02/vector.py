class Vector:
    ### constructor ###
    def __init__(self, arg):
        if type(arg) == int:
            self.shape = (arg, 1)
            self.values = [[float(x)] for x in range(arg)]

        elif type(arg) == tuple:
            if len(arg) != 2:
                print("ERROR: only 2 values accepted in tuple")
                exit(1)
            for x in arg:
                if not isinstance(x, int):
                    print("ERROR: only int accepted in tuple")
                    exit(1)
            if arg[0] >= arg[1]:
                print("ERROR: arg[0] >= arg[1]")
                exit(1)

            self.shape = (arg[1] - arg[0], 1)
            self.values = [[float(x)] for x in range(arg[0], arg[1])]

        elif type(arg) == list:
            if len(arg) == 1:
                self.shape = (1, len(arg[0]))
                self.values = arg
            else:
                self.shape = (len(arg), 1)
                self.values = arg

        else:
            print("ERROR: wrong data type given to Vector")
            exit(1)

    ### 'private' methods ###
    def _is_same_shape(self, vec):
        if not isinstance(vec, Vector):
            print("ERROR: only operation with a vector")
            return 1
        if self.shape != vec.shape:
            print("ERROR: vector has different shape")
            return 1
        return 0

    def _structured_vec(self, flat_vec):
        if self.shape[0] == 1: # row vector
            return Vector([flat_vec])
        else:
            return Vector([[x] for x in flat_vec])

    ### 'public' methods ###

    def dot(self, vec):
        if self._is_same_shape(vec):
            return None
        flat_vec = [y for x in self.values for y in x]
        flat_vec2 = [y for x in vec.values for y in x]
        return sum(x*y for x,y in zip(flat_vec, flat_vec2))

    def T(self):
        # 1st, flatten vector no matter its shape
        flat_vec = [y for x in self.values for y in x]
        # then, return structured vector as opposite of the current shape
        if self.shape[0] == 1:
            return Vector([[x] for x in flat_vec])
        else:
            return Vector([flat_vec])

    ### 'dunder' methods ###

    def __str__(self):
        return f"{str(self.values)}"

    def __repr__(self):
        return f"{str(self.values)}"

    def __mul__(self, other):
        if type(other) != int and type(other) != float:
            print("ERROR: only multiply with a scalar")
            return None
        flat_vec = [(y*other) for x in self.values for y in x]
        return self._structured_vec(flat_vec)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if self._is_same_shape(other):
            return None
        flat_vec = [y for x in self.values for y in x]
        flat_vec2 = [y for x in other.values for y in x]
        flat_vec_add = [x + y for x,y in zip(flat_vec, flat_vec2)]
        return self._structured_vec(flat_vec_add)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self._is_same_shape(other):
            return None
        flat_vec = [y for x in self.values for y in x]
        flat_vec2 = [y for x in other.values for y in x]
        flat_vec_add = [x - y for x,y in zip(flat_vec, flat_vec2)]
        return self._structured_vec(flat_vec_add)

    def __rsub(self, other):
        return self.__sub__(other)

    def __truediv__(self, other):
        if type(other) != int and type(other) != float:
            print("ERROR: only divide with a scalar")
            return None
        if other == 0:
            print("ZeroDivisionError: division by zero.")
            return None
        flat_vec = [(y/other) for x in self.values for y in x]
        return self._structured_vec(flat_vec)

    def __rtruediv__(self, other):
        raise NotImplementedError("Division of a scalar by a "
                                  "Vector is not defined here.")

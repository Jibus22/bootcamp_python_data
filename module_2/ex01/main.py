import random
import string

def what_are_the_vars(*args, **kwargs):
    """ ... """
    new_obj = None
    try:
        new_obj = ObjectC(*args, **kwargs)
    except AttributeError:
        pass
    return new_obj

class ObjectC(object):
    def __init__(self, *args, **kwargs):
        i = 0
        for arg in args:
            attr_name = "var_" + str(i)
            try:
                getattr(self, attr_name)
            except AttributeError:
                setattr(self, attr_name, arg)
            else:
                raise AttributeError
            i += 1

        for kw in kwargs:
            try:
                getattr(self, kw)
            except AttributeError:
                setattr(self, kw, kwargs[kw])
            else:
                raise AttributeError

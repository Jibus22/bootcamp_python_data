import string

def what_are_the_vars(*args, **kwargs):
    """ ... """
    new_obj = ObjectC()
    for i, arg in enumerate(args):
        attr_name = f"var_{i}"
        try:
            getattr(new_obj, attr_name)
        except AttributeError:
            setattr(new_obj, attr_name, arg)
        else:
            return None

    for kw in kwargs:
        try:
            getattr(new_obj, kw)
        except AttributeError:
            setattr(new_obj, kw, kwargs[kw])
        else:
            return None

    return new_obj

class ObjectC(object):
    def __init__(self):
        pass

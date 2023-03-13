def ft_filter(function_to_apply, iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if not callable(function_to_apply):
        raise TypeError(f"{type(function_to_apply)} object is not callable")

    for x in iterable:
        if function_to_apply(x):
            yield x

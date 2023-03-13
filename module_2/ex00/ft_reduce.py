def ft_reduce(function_to_apply, iterable):
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"{type(iterable)} object is not iterable")
    if not callable(function_to_apply):
        raise TypeError(f"{type(function_to_apply)} object is not callable")

    it = iter(iterable)
    value = None
    try:
        value = next(it)
    except StopIteration:
        print(f"TypeError: reduce() of empty sequence with no initial value")
        return None
    for element in it:
        value = function_to_apply(value, element)
    return value

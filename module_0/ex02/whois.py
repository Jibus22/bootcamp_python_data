import sys

try:
    if len(sys.argv) == 1:
        exit(0)
    elif len(sys.argv) > 2:
        raise AssertionError('more than one argument are provided')

    res = int(sys.argv[1])
    if res == 0:
        print("I'm 0")
    elif res % 2 == 0:
        print("I'm even")
    else:
        print("I'm odd")
except AssertionError as err:
    print(f'AssertionError: {err}')
except ValueError as err:
    print(f'ValueError: {err}')
except Exception as err:
    print(f'oopsie hihihi, {type(err)}, {err}')

import time
import math
import os

def log(func):
    def inner(*args, **kwargs):
        begin = time.time()

        ret = func(*args, **kwargs)

        end = time.time()
        elapsed = (end - begin)
        if elapsed >= 1.0:
            unit = "s"
        else:
            elapsed *= 1000
            unit = "ms"
        user = os.getenv("USER")
        if user is None:
            user = ""

        with open('machine.log', 'a') as file:
            file.write(f"({user})Running:"\
                       + f" {func.__name__}".ljust(20)\
                  + f"[ exec-time = {elapsed:.3f} {unit} ]\n")

        return ret
    return inner

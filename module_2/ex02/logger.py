from random import randint
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

        fn_name = func.__name__.split('_')
        fn_name = [x.capitalize() for x in fn_name]
        fn_name = " ".join(fn_name)

        with open('machine.log', 'a') as file:
            file.write(f"({user})Running:"\
                       + f" {fn_name}".ljust(20)\
                  + f"[ exec-time = {elapsed:.3f} {unit} ]\n")

        return ret
    return inner

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)

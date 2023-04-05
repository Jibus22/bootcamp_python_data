class GotCharacter:
    """ A class representing a GOT character """
    def __init__(self, first_name=None, is_alive = True):
        self.first_name = first_name
        self.is_alive = is_alive

class Stark(GotCharacter):
    """ A class representing the Stark family.
    Or when bad things happen to good people. """

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(f"{self.house_words}")

    def die(self):
        self.is_alive = False

class Lannister(GotCharacter):
    """ A class representing the Lannister family. A family full of love """

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear me roar"

    def print_house_words(self):
        print(f"{self.house_words}")

    def die(self):
        self.is_alive = False

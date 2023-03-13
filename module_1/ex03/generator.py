import random

def generator(text, sep=" ", option=None):
    """ Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before
    it is yielded. """

    if not isinstance(text, str) or not isinstance(sep, str):
        print("ERROR")
        return None
    if option != None and not isinstance(option, str):
        print("ERROR")
        return None
    text_list = text.split(sep)

    if option == "unique":
        unique_words = set(word for word in text_list)
        text_list = list(unique_words)
    elif option == "ordered":
        text_list.sort()
    elif option == "shuffle":
        i = 0
        rand_list = []
        while len(text_list) > 0:
            rand_idx = random.randint(0, len(text_list) - 1)
            rand_list.append(text_list[rand_idx])
            text_list.remove(text_list[rand_idx])
        text_list = rand_list

    for word in text_list:
        yield word

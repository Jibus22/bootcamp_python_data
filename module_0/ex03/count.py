import string
import sys

def get_string_details(s):
    upper = lower = punctuation = spaces = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char in string.punctuation:
            punctuation += 1
        elif char == ' ':
            spaces += 1
    return upper, lower, punctuation, spaces

def text_analyzer(s=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text. """

    if s is None:
        s = input('What is the text to analyze?\n')
    elif not isinstance(s, str):
        print(f'AssertionError: Argument is not a string')
        return None
    upper, lower, punctuation, spaces = get_string_details(s)
    print(f'The text contains {len(s)} character(s):\n'
          f'- {upper} upper letter(s)\n'
          f'- {lower} lower letter(s)\n'
          f'- {punctuation} punctuation mark(s)\n'
          f'- {spaces} space(s)')

if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = ' '.join(sys.argv[1:]) # list to string
    else:
        args = None
    text_analyzer(args)

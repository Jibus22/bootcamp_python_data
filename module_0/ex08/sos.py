import sys
import string

args = sys.argv[1:]
if len(args) == 0:
    exit(0)

args = ' '.join(args).lower()
str_filter = string.ascii_lowercase + ' ' + string.digits

if not all(c in str_filter for c in args):
    print('ERROR')
    exit(1)

code_book = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..',
             'e':'.','f':'..-.', 'g':'--.', 'h':'....', 'i':'..',
             'j':'.---','k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.',
             'o':'---','p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...',
             't':'-','u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-',
             'y':'-.--','z':'--..', '0':'-----', '1':'.----', '2':'..---',
             '3':'...--','4':'....-', '5':'.....', '6':'-....', '7':'--...',
             '8':'---..', '9':'----.', ' ': '/'}

print(' '.join([code_book[char] for char in args]))

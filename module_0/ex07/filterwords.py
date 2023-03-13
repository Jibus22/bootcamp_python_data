import sys
import string

args = sys.argv[1:]
nb = 0
if len(args) != 2:
    print('ERROR')
    exit(1)

try:
    nb = int(args[1])
except ValueError as err:
    print('ERROR')
    exit(1)

arg_list = args[0]
for char in string.punctuation:
    arg_list = arg_list.replace(char, "")
arg_list = arg_list.split()
print(f'{[arg for arg in arg_list if len(arg) > nb]}')

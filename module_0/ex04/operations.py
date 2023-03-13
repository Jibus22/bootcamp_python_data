import sys

args = []
try:
    for arg in sys.argv[1:]:
        args.append(int(arg))
except ValueError as err:
    print(f'ValueError: {err}')
    exit(1)

if len(sys.argv) is 1:
    print('Usage: python operations.py <number1> <number2>\n'
          f'Example:\n    python {sys.argv[0]} 10 3')
    exit(0)
if len(sys.argv) is not 3:
    print('AssertionError: wrong number of arguments, 2 required')
    exit(1)

a, b = args[0], args[1]
result = lambda x,y,op : 'ERROR (division by zero)' if y == 0 else f'{x/y}' \
    if op == 1 else f'{x%y}'
print(f'Sum: {a + b}\n'
      f'Difference: {a - b}\n'
      f'Product: {a * b}\n'
      f'Quotient: {result(a,b,1)}\n'
      f'Remainder: {result(a,b,2)}')

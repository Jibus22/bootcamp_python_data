import sys

if len(sys.argv) == 1:
    exit(0)

result = ' '.join(sys.argv[1:]) # list to string
result = result.swapcase()
print(result[::-1]) # reverse

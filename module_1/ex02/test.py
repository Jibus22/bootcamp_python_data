from vector import Vector

l1 = [[0.0], [1.0], [2.0], [6.0]]     #   ----   (4, 1)   ---- column vector
l2 = [[0.0, 1.0, 2.0, 6.0]]           #   ----   (1, 4)   ---- row vector

print(f"{[x[0] for x in l1]}")
print(f"{[x for x in l2[0]]}")

for x in l1:
    for y in x:
        print(y, end=', ')

print()

for x in l2:
    for y in x:
        print(y, end=', ')

print()

print(f"{[y for x in l1 for y in x]}")
print(f"{[y for x in l2 for y in x]}")

v1 = Vector([[0.0], [1.0], [2.0], [6.0]])
v2 = v1 * 5
print(v2)

v1 = Vector([[0.0, 1.0, 2.0, 6.0]])
v2 = v1 * 5
print(v2)

print(v1.dot(v2))

print(v1.values)


print("[1]" + 77*"-")

# Column vector of shape n * 1
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = v1 * 5
print(v2)
# Expected output:
# Vector([[0.0], [5.0], [10.0], [15.0]])
# Row vector of shape 1 * n
v1 = Vector([[0.0, 1.0, 2.0, 3.0]])
v2 = v1 * 5
print(v2)
# Expected output
# Vector([[0.0, 5.0, 10.0, 15.0]])
v2 = v1 / 2.0
print(v2)
# Expected output
# Vector([[0.0], [0.5], [1.0], [1.5]])

# v1 / 0.0
# Expected ouput
# ZeroDivisionError: division by zero.

# 2.0 / v1
# Expected output:
# NotImplementedError: Division of a scalar by a Vector is not defined here.

print("[2]" + 77*"-")

# Column vector of shape (n, 1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).shape)
# Expected output
# (4,1)
print(Vector([[0.0], [1.0], [2.0], [3.0]]).values)
# Expected output
# [[0.0], [1.0], [2.0], [3.0]]
# Row vector of shape (1, n)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).shape)
# Expected output
# (1,4)
print(Vector([[0.0, 1.0, 2.0, 3.0]]).values)
# Expected output
# [[0.0, 1.0, 2.0, 3.0]]

print("[3]" + 77*"-")

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
print(v1.shape)
# Expected output: (4,1)
print(v1.T())
# Expected output:
# Vector([[0.0, 1.0, 2.0, 3.0]])
print(v1.T().shape)
# Expected output: # (1,4)
# Example 2:
v2 = Vector([[0.0, 1.0, 2.0, 3.0]])
print(v2.shape)
# Expected output:
# (1,4)
print(v2.T())
# Expected output:
# Vector([[0.0], [1.0], [2.0], [3.0]])
print(v2.T().shape)
# Expected output: # (4,1)

print("[4]" + 77*"-")

# Example 1:
v1 = Vector([[0.0], [1.0], [2.0], [3.0]])
v2 = Vector([[2.0], [1.5], [2.25], [4.0]])
print(v1.dot(v2))
# Expected output:
# 18.0
v3 = Vector([[1.0, 3.0]])
v4 = Vector([[2.0, 4.0]])
print(v3.dot(v4))
# Expected output:
# 13.0
v1
# Expected output: to see what __repr__() should do
# [[0.0, 1.0, 2.0, 3.0]]
print(v1)
# Expected output: to see what __str__() should do
# [[0.0, 1.0, 2.0, 3.0]]

print("[5]" + 77*"-")

v5 = v1 + v2
v6 = v5 - v1

print(v5)
#[[2.0], [2.5], [4.25], [7.0]]
print(v6)
#[[2.0], [1.5], [2.25], [4.0]]

v7 = 5 * v1
print(v7)

v8 = v2 / 0.0
print(v8)

try :
    v9 = 2.3 / v2
except NotImplementedError as err:
    print(f'NotImplementedError : {err}')

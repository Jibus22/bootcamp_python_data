from ft_map import ft_map
from ft_filter import ft_filter
from ft_reduce import ft_reduce
from functools import reduce

print("\n[ft_map]"  + 72 * "-") #########################################

lst = [1, 2, 3, 4]
lst2 = ['aa', 'bb', 'cc']

def multiply_2(x):
    return x * 2
def cap(x):
    return x.capitalize()

u = ft_map(cap, lst2)
print(u)
print(list(u))
y = ft_map(multiply_2, lst)
print(y)
print(list(y))

print("\n[ft_filter]"  + 68 * "-") #######################################

x = [1, 2, 3, 4, 5]

print(ft_filter(lambda dum: not (dum % 2), x))
print(list(ft_filter(lambda dum: not (dum % 2), x)))

print("\n[ft_reduce]"  + 68 * "-") #######################################

lst = ["H", "e", "l", "l", "o", " ", "w", "o", "r", "l", "d"]

def accu(u, v):
    return u + v
def mult(u, v):
    return u * v

res = ft_reduce(accu, lst)
print(type(res))
print(res)

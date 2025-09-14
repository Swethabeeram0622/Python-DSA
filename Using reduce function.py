# Using reduce function
from functools import reduce
def add(x,y):
    return x+y
numbers = (1, 2, 3, 4, 5)
x = reduce(add,numbers)
print(int(x))

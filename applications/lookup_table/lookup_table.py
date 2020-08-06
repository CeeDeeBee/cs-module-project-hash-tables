import math
import random
from hashtable import HashTable
# Your code here
cache = HashTable(8)


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    key = str(x) + str(y)
    value = cache.get(key)
    if value:
        return value

    value = slowfun_too_slow(x, y)
    cache.put(key, value)

    return value


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')

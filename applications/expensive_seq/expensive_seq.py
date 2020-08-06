# Your code here
from hashtable import HashTable

cache = HashTable(8)


def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        return y + z

    key1 = str(x-1) + str(y+1) + str(z)
    key2 = str(x-2) + str(y+2) + str(z*2)
    key3 = str(x-3) + str(y+3) + str(z*3)

    val1 = cache.get(key1)
    val2 = cache.get(key2)
    val3 = cache.get(key3)

    if not val1:
        val1 = expensive_seq(x-1, y+1, z)
        cache.put(key1, val1)

    if not val2:
        val2 = expensive_seq(x-2, y + 2, z*2)
        cache.put(key2, val2)

    if not val3:
        val3 = expensive_seq(x-3, y+3, z*3)
        cache.put(key3, val3)

    return val1 + val2 + val3


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

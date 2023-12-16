''' lru_cache
The lru_cache decorator is used for memoization, which is a technique to cache the results of a function so that if the same inputs are provided again, the function can return the cached result instead of recomputing it. This can significantly improve the performance of functions, especially recursive or computationally expensive ones.
'''
from functools import lru_cache

@lru_cache(maxsize=None)  # None means no limit on cache size
def add(a, b):
    print(f'Adding {a}, {b}')
    return a + b

result = add(10, 5)
print(result)  

result = add(10, 5)
print(result)

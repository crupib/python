from functools import lru_cache
from datetime import datetime
@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start_time = datetime.now()
print(fibonacci(50))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))

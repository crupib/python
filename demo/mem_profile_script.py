#my_script.py

from memory_profiler import profile

@profile
def add():
    a = [1] * (10 ** 1)
    b = [2] * (3 * 10 ** 2)
    sum = a+b
    return sum

if __name__ == '__main__':
    add()

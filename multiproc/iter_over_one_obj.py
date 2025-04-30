# iteration function that takes as input a value from iterable and returns an output
iterable = range(0,1000000)

def func(n):
    # Real hard work here
    return n**2
def execute_func_using_verstack():
    from verstack import Multicore
    worker = Multicore()
    result = worker.execute(func, iterable)
if __name__ == '__main__':
    execute_func_using_verstack()

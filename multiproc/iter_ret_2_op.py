# iteration function that takes as input a value from iterable and returns an output
iterable = range(0,10)

def return_two_outputs(n):
    # Real hard work here
    return n**2, n**3
def execute_func_using_verstack():
    from verstack import Multicore
    worker = Multicore()
    result = worker.execute(return_two_outputs, iterable)
    print(result)
if __name__ == '__main__':
    execute_func_using_verstack()

# added pickle.dump the result to local directory

iterable = range(0,1000000)

def func(n):
    # Real hard work here
    return n**2

def execute_func_using_verstack():
    from verstack import Multicore
    import pickle
    worker = Multicore()
    result = worker.execute(func, iterable)
    pickle.dump(result, open('iteration_result.p', 'wb'))

if __name__ == '__main__':
    execute_func_using_verstack()

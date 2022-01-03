# added pickle.dump the result to local directory
import pickle
iterable = range(0,1000000)
iterable2 = range(0,0)
def func(n):
    # Real hard work here
    return n**2
def pikfund(n):
    result = None
    pickle.dump(result, open('ver.p','wb'))
    return n
def execute_func_using_verstack():
    from verstack import Multicore
    worker = Multicore()
    result = worker.execute(func, iterable)
    piksult = worker.execute(pikfund,iterable2)

if __name__ == '__main__':
    execute_func_using_verstack()

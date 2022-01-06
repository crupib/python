# added pickle.dump the result to local directory
iterable0 = range(0,10)
iterable1 = range(10,20)
iterable2 = range(20,30)
def process_multiple_iterables(x,y,z):
    # Real hard work here
    result_0 = x**2
    result_1 = y**2
    result_2 = z**2
    return result_0, result_1, result_2

def execute_func_using_verstack():
    from verstack import Multicore
    worker = Multicore(multiple_iterables = True, workers = 2)
    result = worker.execute(process_multiple_iterables, [iterable0, iterable1, iterable2])
    print(result)

if __name__ == '__main__':
    execute_func_using_verstack()

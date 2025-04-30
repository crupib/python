# iteration function that takes as input a value from iterable and returns an output

dictionary = {'a':list(range(75,100))}
iterable = list(range(50,100))

def include_dictionary(dictionary,iterable):
    # Real hard work here
    result = []
    for item in iterable:
        if item in list(dictionary.values())[0]:
           result.append(item**3)
    return result
def execute_func_using_verstack():
    from verstack import Multicore
    worker = Multicore(workers = 2)
    result = worker.execute(include_dictionary, iterable, dictionary)
    print(result)
if __name__ == '__main__':
    execute_func_using_verstack()

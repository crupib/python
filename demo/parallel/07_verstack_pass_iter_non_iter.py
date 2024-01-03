# Pass one iterable and one non_iterable object
# function will iterate over iterable list and if value is present in dictionary
    # will perform calculations on item
dictionary = {'a':list(range(50,100))}
iterable = list(range(50,100))

def include_dictionary(dictionary, iterable):
    # Real hard work here
    result = []
    for item in iterable:
        if item in list(dictionary.values())[0]:
            result.append(item**3)
    return result
def main():

  from verstack import Multicore
  worker = Multicore()
  result = worker.execute(include_dictionary, iterable, dictionary)
  print(result)

if __name__ == "__main__":
   main()

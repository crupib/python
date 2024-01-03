# iterate over multiple iterables
iterable1 = range(0,10)
iterable2 = range(10,20)
iterable3 = range(20,30)

def process_multiple_iterables(lst1, lst2, lst3):
    result_1 = lst1**2
    result_2 = lst2**2
    result_3 = lst3**2
    result = result_1 + result_2 + result_3
    return result
def main():
  from verstack import Multicore
  # notice the multiple_iterables parameter
  worker = Multicore(multiple_iterables = True) 
  # notice how multiple iterables are passed in a list
  result = worker.execute(process_multiple_iterables, [iterable1, iterable2, iterable3])
  print(result)

if __name__ == "__main__":
     main()


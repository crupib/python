import timeit
def binary_search(list, item):
   low = 0
   high = len(list)
   while (low <= high):
     mid = (low + high) // 2
     guess = list[mid]
     if guess == item:
       return mid
     if guess > item:
       high = mid - 1
     else:
       low = mid + 1
   return None
def main():
   mylist = [1,3,5,7,9,11,15, 20, 25, 30, 60, 100]
   start = timeit.default_timer()
   print(binary_search(mylist, 3))
   print(timeit.default_timer() - start)
#   start = timeit.default_timer()
#   print(binary_search(mylist, 30))
#   print(timeit.default_timer() - start)
if __name__ == "__main__":
    main()

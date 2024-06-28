import timeit

list_1object=[]
list_2object=[]
def do_1():
  for i in range(100):
    list_1object.append(i)
def do():
    [list_2object.append(i) for i in range(100)]
def main():
  start = timeit.default_timer()
  do_1()
  time1 = timeit.default_timer() - start
  print("ordinary list appends ",time1)
  start = timeit.default_timer()
  time2 = timeit.default_timer() - start
  do()
  print("list comp", time2)
  print(max(time1,time2))
  print(min(time1,time2))
if __name__ == "__main__":
    main()

from memory_profiler import profile
import multiprocessing
import time
@profile
def my_function():
    for i in range(5):
        print("Process executing", i)
        time.sleep(1)

if __name__ == '__main__':
  try:
    p1 = multiprocessing.Process(target=my_function)
    p2 = multiprocessing.Process(target=my_function)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
  except AttributeError:
    print("Program completed")

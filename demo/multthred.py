from memory_profiler import profile
import threading
import time
@profile
def my_function():
    for i in range(5):
        print("Thread executing", i)
        time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=my_function)
    t2 = threading.Thread(target=my_function)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Program completed")

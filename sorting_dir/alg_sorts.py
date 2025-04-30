from algorithms.sort import merge_sort
from algorithms.sort import insertion_sort
from algorithms.sort import selection_sort
from algorithms.sort import quick_sort
from algorithms.sort import bubble_sort
from algorithms.sort import shell_sort
from algorithms.sort import radix_sort
from algorithms.sort import heap_sort
import time
from random import randint
ARRAY_LENGTH = 10000
if __name__ == "__main__":
#   merge sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = merge_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for merge sort",eot-sot)
    print(my_list[:10])
#   insertion sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = insertion_sort(my_list)
    print(my_list[:10])
    eot = time.perf_counter()
    print("Total run time for insertion sort",eot-sot)
#   selection sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = selection_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for selection sort",eot-sot)
    print(my_list[:10])
#   quick sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = quick_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for quick sort",eot-sot)
    print(my_list[:10])
#   bubble sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = bubble_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for bubble sort",eot-sot)
    print(my_list[:10])
#   shell sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = shell_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for shell sort",eot-sot)
    print(my_list[:10])
#   radix sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = radix_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for radix sort",eot-sot)
    print(my_list[:10])
#   heap sort
    my_list = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    print(my_list[:10])
    sot = time.perf_counter()
    my_list = heap_sort.max_heap_sort(my_list)
    eot = time.perf_counter()
    print("Total run time for heap sort",eot-sot)
    print(my_list[:10])

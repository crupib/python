import matplotlib.pyplot as plt
import time
import random

def bubble_sort(lst):
    lst = lst[:]  # Copy to avoid mutating the input
    for passLeft in range(len(lst) - 1, 0, -1):
        for i in range(passLeft):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def qsort(lst):
    if not lst:
        return []
    pivot = lst[0]
    lesser = [x for x in lst[1:] if x <= pivot]
    greater = [x for x in lst[1:] if x > pivot]
    return qsort(lesser) + [pivot] + qsort(greater)

def timsort(lst):
    return sorted(lst)

def create_random_list(n):
    return random.sample(range(n), n)

n = 500
xs = list(range(1, n + 1, n // 10))
y_bubble = []
y_qsort = []
y_tim = []

for x in xs:
    lst = create_random_list(x)
    start_time = time.time()
    bubble_sort(lst)
    y_bubble.append(time.time() - start_time)

    start_time = time.time()
    qsort(lst)
    y_qsort.append(time.time() - start_time)

    start_time = time.time()
    timsort(lst)
    y_tim.append(time.time() - start_time)

plt.plot(xs, y_bubble, '-x', label='bubblesort')
plt.plot(xs, y_qsort, '-o', label='qsort')
plt.plot(xs, y_tim, '--', label='timsort')
plt.grid()
plt.xlabel('List Size (No. Elements)')
plt.ylabel('Runtime (s)')
plt.legend()
plt.show()

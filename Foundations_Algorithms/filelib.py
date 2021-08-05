import random
from streamlit import caching
import sys
import struct
import time
from datetime import datetime
def quickSort(dataset, first, last):
    if first < last:
        # calculate the split point
        pivotIdx = partition(dataset, first, last)

        # now sort the two partitions
        quickSort(dataset, first, pivotIdx-1)
        quickSort(dataset, pivotIdx+1, last)
def partition(datavalues, first, last):
    # choose the first item as the pivot value
    pivotvalue = datavalues[first]
    # establish the upper and lower indexes
    lower = first + 1
    upper = last
    # start searching for the crossing point
    done = False
    while not done:
        # advance the lower index
        while lower <= upper and datavalues[lower] <= pivotvalue:
            lower += 1
        # advance the upper index
        while datavalues[upper] >= pivotvalue and upper >= lower:
            upper -= 1
        # if the two indexes cross, we have found the split point
        if upper < lower:
            done = True
        else:
            # exchange the two values
            temp = datavalues[lower]
            datavalues[lower] = datavalues[upper]
            datavalues[upper] = temp

    # when the split point is found, exchange the pivot value
    temp = datavalues[first]
    datavalues[first] = datavalues[upper]
    datavalues[upper] = temp
    # return the split point index
    return upper



def random_Write(num):
# Open a file  for writing 
    with open('random.bin', 'wb') as file:
       for i in range(0,num):
          rand = random.randint(0,100)
          file.write((rand).to_bytes(4,byteorder='big', signed=False))
        #closing file
    file.close()
def create_random(num):
    array = []
    random.seed("re-seed baby")
    for i in range(0,num):
       rand = random.randint(0,10000)
       array.append(rand)
    return array
def random_Read():
#Reading from file
    with open('random.bin', 'rb') as file:
       for chunk in iter(lambda: file.read(4), ''):
          integer_value = struct.unpack('<I',chunk)[0]
          print(integer_value)
    file.close()
def main():
    num = int(input("How many numbers would you like to generate?: "))
    sys.setrecursionlimit(1000000000)
    print("Recursion limit after set ",sys.getrecursionlimit())
    caching.clear_cache()
    start = time.time()
    myarray= create_random(num)
    end = time.time()
    print("\nRunning time for create\n",(end-start)/60)
    start = time.time()
#    quickSort(myarray, 0, len(myarray)-1)
    mysortedarray = sorted(myarray)
    end = time.time()
    print("\nRunning time for sort\n",(end-start)/60)
#    with open('sorted_rand.txt','w') as f:
#        for item in myarray:
#            f.write(str(item)+'\n')
    with open('sorted_rand_sys.txt','w') as f:
        for item in mysortedarray:
            f.write(str(item)+'\n')
main()

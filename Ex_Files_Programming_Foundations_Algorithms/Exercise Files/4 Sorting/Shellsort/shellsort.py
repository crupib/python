# shell sort algorithm

def shellSort(list):
    # start with the array length and decrement each time
    distance = len(list) // 2
    while distance > 0:
      for i in range(distance, len(list)):
        temp = list[i]
        j = i
        while j >= distance and list[j - distance] > temp:
          list[j] = list[j- distance]
          j = j - distance
        list[j] = temp
      distance = distance // 2
    return list 
def main():
    list1 = [26,17,20,11,23,21,13,18,24,12,22,16,15,19,25]
    print("Starting state: ", list1)
    shellSort(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()

def shellSort(list):
    # start with the array length and decrement each time
    distance = len(list) // 2
    while distance > 0:
      for i in range(distance, len(list)):
        temp = list[i]
        j = i
        while j >= distance and list[j - distance][4] > temp[4]:
          list[j] = list[j- distance]
          j = j - distance
        list[j] = temp
      distance = distance // 2
    return list

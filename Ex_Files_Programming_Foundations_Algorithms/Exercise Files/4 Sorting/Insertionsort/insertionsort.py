# insert sort algorithm


def insertion(list):
    for i in range(1,len(list)):
        j = i-1
        element_next = list[i]
        while (list[j] > element_next):
          list[j+1] = list[j]
          j=j-1
        list[j+1] = element_next
    return list

def main():
    list1 = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    print("Starting state: ", list1)
    insertion(list1)
    print("Final state: ", list1)


if __name__ == "__main__":
    main()

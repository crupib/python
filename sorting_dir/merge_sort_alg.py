from algorithms.sort import merge_sort

if __name__ == "__main__":
    my_list1 = [1, 8, 3, 5, 6]
    my_list2 = [1, 9, 7, 5, 6]
    my_combined = my_list1+my_list2
    my_list = merge_sort(my_combined)
    print(my_list)

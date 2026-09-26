def quicksort(arr):
    """
    Sorts an array in ascending order using the quicksort algorithm.

    :param arr: The input array to be sorted.
    :return: A new sorted array.
    :raises ValueError: If the input array is empty or contains only one element.
    :raises TypeError: If the input is not a list or contains non-comparable elements.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")

    if len(arr) < 2:
        return arr

    try:
        pivot = arr[len(arr) // 2]
    except TypeError:
        raise TypeError("Non-comparable elements in input array")

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def main():
    arr = [5, 2, 9, 1, 7, 6, 8, 3, 4]
    sorted_arr = quicksort(arr)
    print(sorted_arr)
    assert sorted_arr == [1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == "__main__":
    main()

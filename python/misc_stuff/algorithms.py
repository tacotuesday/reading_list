from typing import List, Any


def binary_search(source_list, item):
    """
    Simple binary search implementation. O(log n). List must be ordered.
    :param source_list: List of items in which to search.
    :param item: Item for which you're searching in the list.
    :return: Index of item if found. None if item is not found.
    """
    low = 0
    high = len(source_list) - 1          # Defines initial search window
    while low <= high:
        mid = (low + high) // 2
        guess = source_list[mid]         # `guess` = middle of the search window
        if guess == item:         # Item found
            return mid
        if guess > item:          # Target less than the middle of the window
            high = mid - 1        # Reduce the high end of the window
        else:
            low = mid + 1         # Increase the low end of the window
    return None


def find_smallest(arr: object):
    """
    Find the index of the smallest element in an array.
    :type arr: object
    :param arr: Integer array
    :return: Index of the smallest number in the array
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    """
    Simple selection sort implementation.
    :param arr: Array of elements from which to select
    :return: Sorted array
    """
    new_arr: list[Any] = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))       # Remove `smallest` from `arr` and append it to `new_arr`
    return new_arr


def quicksort(array):
    """
    Simple quicksort implementation. Note the fixed pivot on the first element of the array.
    :param array: Array of numbers
    :return: Array of numbers sorted ascending order
    """
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i >= pivot]
        return quicksort(less) + [pivot] + quicksort(greater)







arr = [13, 46, 24, 52, 20 ,9]

# Selection sort - selected minimal and swape
def selection_sort(arr):
    """
    Sorts an array using the Selection Sort algorithm.
    Selection Sort is an in-place comparison-based sorting algorithm that divides 
    the input array into two parts: a sorted subarray and an unsorted subarray. 
    It repeatedly finds the minimum element from the unsorted subarray and places 
    it at the beginning of the unsorted subarray.
    Args:
        arr (list): A list of comparable elements to be sorted.
    Returns:
        list: The input array sorted in ascending order.
    Time Complexity:
        - Best Case: O(n²)
        - Average Case: O(n²)
        - Worst Case: O(n²)
    Space Complexity:
        O(1) - Sorts in-place with constant extra space.
    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]
        >>> selection_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    Note:
        This algorithm is unstable and not suitable for large datasets due to 
        its O(n²) time complexity. It is useful for small arrays or when memory 
        usage is a concern.
    """

    n = len(arr)

    for i in range(n - 1):
        min = i

        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr

# arr = [13, 46, 24, 52, 20 ,9]
# print(selection_sort(arr))

# Bubble sorting - push the max to the last by adjacent swaps
def bubble_sort(arr):
    """
    Sorts an array in ascending order using the Bubble Sort algorithm.
    Bubble Sort is a simple comparison-based sorting algorithm that repeatedly
    steps through the list, compares adjacent elements, and swaps them if they
    are in the wrong order. The algorithm continues until no more swaps are needed,
    indicating that the array is sorted.
    Args:
        arr (list): A list of comparable elements (integers, floats, strings, etc.)
                   to be sorted in ascending order.
    Returns:
        list: The sorted array in ascending order.
    Time Complexity:
        - Best Case: O(n) - when the array is already sorted
        - Average Case: O(n²) - typical case with random data
        - Worst Case: O(n²) - when the array is sorted in descending order
    Space Complexity:
        O(1) - sorts in-place with only a constant amount of extra space
    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        >>> bubble_sort([5, 2, 8, 1, 9])
        [1, 2, 5, 8, 9]
    Note:
        This implementation includes an optimization flag (did_swap) to detect
        if the array is already sorted and terminate early, improving best-case
        performance from O(n²) to O(n).
    """

    n = len(arr)

    # range(start, stop, step)
    for i in range(n - 1, 0, -1):
        did_swap = 0

        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = 1
        
        if did_swap == 0:
            break

    return arr

# arr = [13, 46, 24, 52, 20 ,9]
# print(bubble_sort(arr))

# Insertion Sorting - Take an element & place it in its correct order
def insertion_sort(arr):
    """
    Sorts an array in ascending order using the insertion sort algorithm.
    Insertion sort builds the final sorted array one item at a time by iterating
    through the array and inserting each element into its correct position among
    the previously sorted elements.
    Args:
        arr (list): A list of comparable elements to be sorted.
    Returns:
        list: The same list sorted in ascending order (in-place modification).
    Time Complexity:
        - Best case: O(n) - when the array is already sorted
        - Average case: O(n²)
        - Worst case: O(n²) - when the array is sorted in reverse order
    Space Complexity:
        O(1) - sorts in-place, requires only constant additional space
    Example:
        >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)

    for i in range(n):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1

    return arr

# print(bubble_sort(arr))

# Merge Sort - Divide and Merge
def merge_sort(arr, low, high):
    """
    Merge Sort Algorithm
    This function implements the merge sort algorithm, which is a divide-and-conquer 
    sorting technique. It recursively divides the input array into two halves, sorts 
    each half, and then merges the sorted halves back together.
    Parameters:
        arr (list): The list of elements to be sorted.
        low (int): The starting index of the subarray to be sorted.
        high (int): The ending index of the subarray to be sorted.
    Returns:
        list: The sorted list of elements.
    Usage:
        To sort an array, call merge_sort(arr, 0, len(arr) - 1).
    """

    if low >= high:
        return
    
    mid = (low + high) // 2

    merge_sort(arr, low, mid)
    merge_sort(arr, mid + 1, high)
    merge(arr, low, mid, high)

    return arr

def merge(arr, low, mid, high):
    """
    Merge function to merge two sorted subarrays of a given array.
    Parameters:
        arr (list): The array containing the subarrays to be merged.
        low (int): The starting index of the first subarray.
        mid (int): The ending index of the first subarray and the starting index of the second subarray.
        high (int): The ending index of the second subarray.
    Returns:
        list: The merged array with elements sorted in non-decreasing order.
    The function works by comparing the elements of the two subarrays and
    appending the smaller element to a temporary list, which is then copied
    back to the original array.
    """

    left = low
    right = mid + 1
    tmp = []

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            tmp.append(arr[left])
            left += 1
        else:
            tmp.append(arr[right])
            right += 1

    while left <= mid:
        tmp.append(arr[left])  
        left += 1      

    while right <= high:
        tmp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = tmp[i - low]

    return arr

# print("merger sorting", merge_sort(arr, 0, len(arr) - 1))

# Quick sort
def quick_sort(arr, low, high):
    """
    Quick Sort Algorithm
    This function implements the Quick Sort algorithm to sort an array in ascending order.
    Parameters:
        arr (list): The list of elements to be sorted.
        low (int): The starting index of the portion of the list to be sorted.
        high (int): The ending index of the portion of the list to be sorted.
    Returns:
        list: The sorted list.
    The function uses a recursive approach to sort the elements by selecting a 'pivot'
    and partitioning the array into elements less than and greater than the pivot.
    """

    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index - 1)
        quick_sort(arr, p_index + 1, high)

    return arr

def partition(arr, low, high):
    """
    Partition the array into two halves based on a pivot element.
    This function selects a pivot element from the array and partitions the
    other elements into two sub-arrays according to whether they are less
    than or greater than the pivot. The pivot is chosen as the first element
    of the array.
    Parameters:
        arr (list): The list of elements to be partitioned.
        low (int): The starting index of the sub-array to be partitioned.
        high (int): The ending index of the sub-array to be partitioned.
    Returns:
        int: The index of the pivot element after partitioning.
    """

    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

arr2 = [13, 46, 24, 52, 20 ,9]
print("quick_sort", quick_sort(arr2, 0, len(arr2) - 1))

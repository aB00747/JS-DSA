# Selection Sort - selected minimal & swape


def selection_sort(arr):
    n = len(arr)
    # print("length",n)

    for i in range(n - 1):
        print("i", i)
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # print("after swape", arr, "I", i, "j", min_index)
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


element = [13, 46, 24, 52, 20, 9]
# element = [2, 20, 25, 9, 7, 44]
# print(selection_sort(element))


def selection_sort2(arr):
    n = len(arr)
    for i in range(n - 1):
        # print(i)
        min_val_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_val_index]:
                min_val_index = j

        arr[i], arr[min_val_index] = arr[min_val_index], arr[i]

    return arr


# print(selection_sort2(element))


def bubble_sort(arr):
    n = len(arr)
    for i in range(n, 0, -1):
        didSwap = 0
        for j in range(i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                didSwap = 1

        if didSwap == 0:
            break

    return arr


# print(bubble_sort(element))


def inseration_sort(arr):
    n = len(arr)

    for i in range(n):
        j = i

        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1

    return arr

# print(inseration_sort(element))



def merge(arr, low, mid, high):
    # print("calling merge!!")
    # merge the array
    temp = []
    left = low
    right = mid + 1

    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    while left <= mid:
        temp.append(arr[left])
        left += 1

    while right <= high:
        temp.append(arr[right])
        right += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    # return arr


def mergeSort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    # n = len(arr)
    if low >= high:
        return
    
    mid = (low + high) // 2

    # left
    mergeSort(arr, low, mid)
    # right
    mergeSort(arr, mid + 1, high)
    # merge the arrays
    # return merge(arr, low, mid, high)
    merge(arr, low, mid, high)

    # return arr

# print(len(element) - 1)
print("before merge Sorted array:", element)
print(mergeSort(element, 0, len(element) - 1))
print("merge Sorted array:", element)


for i in range(5, 8):
    # print(i)
    print(i - 5)




x = 'Welcome'
y = 'Coders'
print(x + y)
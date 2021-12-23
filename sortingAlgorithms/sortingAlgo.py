def bubbleSort(arr: list):
    n = len(arr)

    for i in range(n):
        isSorted = True
        for j in range(1, n - i):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                isSorted = False
        if isSorted:
            return


def selectionSort(arr: list):
    n = len(arr)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def insertionSort(arr: list):
    n = len(arr)

    for i in range(1, n):
        curr = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = curr


def merge(left, right, arr):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


def mergeSort(arr: list):
    if len(arr) < 2:
        return
    # divide into two halfs.
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # sort two halfs.
    mergeSort(left)
    mergeSort(right)
    # merge two halfs.
    merge(left, right, arr)


def partition(arr, start, end):
    pivot = arr[end]
    boundary = start - 1
    for i in range(start, end + 1):
        if arr[i] <= pivot:
            boundary += 1
            arr[i], arr[boundary] = arr[boundary], arr[i]
    return boundary


def quickSort(arr, start, end):
    if start >= end:
        return
    boudary = partition(arr, start, end)
    quickSort(arr, start, boudary - 1)
    quickSort(arr, boudary + 1, end)


nums = [3, 6, 2, 9, 4, 5, -1, 10, 3, 2]

quickSort(nums, 0, len(nums) - 1)
print(nums)
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


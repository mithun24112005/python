# insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]  # exchanging values of j-1 and j
            j -= 1
    return arr


arr = [2, 34, 53, 78, 96, 45, 36, 12]
print(insertion_sort(arr))

# # insertion sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         j = i
#         while arr[j - 1] > arr[j] and j > 0:
#             arr[j - 1], arr[j] = arr[j], arr[j - 1]  # exchanging values of j-1 and j
#             j -= 1
#     return arr


# arr = [2, 34, 53, 78, 96, 45, 36, 12]
# print(insertion_sort(arr))

def insertion(arr):
    n=len(arr)

    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1],arr[j]=arr[j],arr[j-1]  #exchanging values
            j-=1
            arr[j+1]=key
    return arr

arr=[12,23,43,53,24,5,15,6,8,90]
print(insertion(arr))


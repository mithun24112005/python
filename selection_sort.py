# selection sort
# def selectionsort(l):
#     for start in range(len(l)):
#         for i in range(start, len(l)):
#             minpos = start
#             if l[i] < l[minpos]:
#                 minpos = i
#                 (l[start], l[minpos]) = (l[minpos], l[start])
#     return l


# l = list(range(1000, 0, -1))
# print(selectionsort(l))

def selection(arr):
    n=len(arr)
    for i in range(n-1):
        mini=1
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
# find least index with j and assign mini to j and swap it with index i
                mini=j
                arr[i],arr[mini]=arr[mini],arr[i]
    return arr

arr=[12,23,43,53,24,5,15,6,8,90]
print(selection(arr))
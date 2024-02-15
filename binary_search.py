# binary search using python

# STEPS

# a function that takes list and target parameter
# variables: middle, start, end, steps
# recurssion or while loop
# increase steps each tome a split is done


def binary_search(arr, key):
    low=0
    high=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            high=mid-1
        elif arr[mid]<key:
            low=mid+1
    return -1



arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

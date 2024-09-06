# selection sort
def selectionsort(l):
    for start in range(len(l)):
        for i in range(start, len(l)):
            minpos = start
            if l[i] < l[minpos]:
                minpos = i
                (l[start], l[minpos]) = (l[minpos], l[start])
    return l


l = list(range(1000, 0, -1))
print(selectionsort(l))

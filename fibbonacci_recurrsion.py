import time

def fibiter(num):
    prevn=0
    currn=1
    for i in range(1,num):
        preprevn=prevn
        prevn=currn
        currn=prevn+preprevn
    return currn
    pass

def fibrecur(num):
    if num==0:
        return 0
    elif (num==1):
        return 1
    else:
        return fibrecur(num-1)+fibrecur(num-2)

num=int(input("enter the number: "))
init=time.time()
# print(f"recuesive approach: value of fib({num}) is: {fibrecur(num)}")
print(f"iter approach: value of fib({num}) is: {fibiter(num)}")
print(f"it took: {time.time()-init}")
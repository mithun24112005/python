def factorial(n):
    if n<0:
        return "invalid no"
    elif n<=1:
        return 1
    else:
        r=1
        for i in range(1,n+1):
            r=r*i
        return r

def factrailoo(n): # to find trailing zeros in factorial by dividing by ten
    r=factorial(num)
    count=0
    while r%10==0:
        count=count+1
        r=r/10
    return count

def factrailingzero(n):
    count=0
    # 100!=100//5+100//5*5
    i=5
    while n//i!=0:
        count+=int(num/i)
        i=i*5
    return count

num=int(input("enter the no: "))
if num<=10:
    print(f"the factorial of the no {num} is: {factorial(num)}")
    print(f"the number of trailing zeros in {factorial(num)} is: {factrailoo(num)}")
else:
    print(f"this is bigg no.\nthe number of trailing zeros is:{factrailingzero(num)}")


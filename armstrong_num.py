# xyz.. = x^n+y^n+z^n # n-->number of digits then it is a armstrong num of order num
n=int(input("enter the num: "))
def armstrong(num):
    order=len(str(num))
    copy=num
    sum=0
    i=0
    while (i<=order):
        digit=num%10
        sum+=(digit**order)
        num=num//10
        i+=1
    if (sum==copy):
        print(f"{copy} is an armstrong number")
    else:
        print(f"{copy} is not an armstrong number")
armstrong(n)

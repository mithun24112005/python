n1=int(input("enter 1st num: "))
n2=int(input("enter 2nd num: "))
min=min(n1,n2)
print(f"the min num is: {min}")
for i in range(1,min+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print(f"the hcf/gcd of nums {n1} and {n2} is: {hcf}")

n1=int(input("enter 1st num: "))
n2=int(input("enter 2nd num: "))
multiple=0
i=1
while True:
    multiple=n1*i
    if multiple%n2==0:
        print(f"the lcm of the numbers {n1} and {n2} is: {multiple}")
        break
    else:
        i+=1


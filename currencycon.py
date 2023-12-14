with open ('currency.txt') as f:
    lines=f.readlines()
currdict={}
print(lines)
for line in lines:
    parsed=line.split("\t")
    currdict[parsed[0]]=parsed[1]
    break
amt=int(input("enter amt: "))
print("enter the name of currency u want to convert to: \n")
for item in currdict.keys():
    print(item)
currency=input("please enter one of the values: \n ")
print(f"{amt} INR is equal to {amt*float(currdict[currency])} {currency}")
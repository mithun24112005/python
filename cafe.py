# define a menu of restaurant
menu ={'pizza':40,'pasta':50,'burger':60,'salad':70,'coffee':80}

# greet 
print("welcome to python restront")
for item,prize in menu.items():
    print(f"{item}: Rs{prize}")

order_total=0
no_items=int(input("enter the number of items: "))
items=[]
for i in range(no_items):
    while True:
        temp=input("enter the name of item: ")
        if temp in menu:
            print(f"your item {temp} is added to ur order")
            items.append(temp)
            order_total+=menu[temp]
            break
        else:
            print("item not in menu, try again")
print("the total ordered items are:")
for i in range(no_items):
    print(items[i],menu[items[i]])
print("the total bill is: ",order_total)

# add functionality of adding the same item for many times
# like 2 pizzas 5 burgers etc
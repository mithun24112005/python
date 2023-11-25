import random
op=['s','w','g','q']
cwin=0
uwin=0
while True:
    cop=['s','w','g']
    cin=random.choice(cop)
    uin=input("enter 's' or 'w' or 'g' or 'q' to quit: ")
    if uin not in op:
        print("invalid input")
        break
    elif uin in op and uin!='q':
        if ((uin=='s' and cin=='w') or (uin=='w' and cin=='g') or (uin=='g' and cin=='s')):
            uwin+=1
            print("u win!!")
        else:
            cwin+=1
            print("u lose")
    elif uin=='q':
        print("your score: ",uwin)
        print("u win") if uwin>cwin else print("draw") if uwin==cwin else print("u lose")
        break






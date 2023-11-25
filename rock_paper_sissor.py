import random

usrw =  0 
compwin=0
options = ["rock","paper","sissor"]
while True:
    usrin = input("type rock/paper/sissor/quit : ").lower()
    if usrin == "quit":
        break;

    if usrin not in ["rock","paper","sissor","quit"]:
        print("invalid")
        continue
    rn = random.randint(0,2)
    cp = options[rn]
    print("computer picked",cp+".")

    if (usrin == "rock" and cp == "sissor") or (usrin == "paper" and cp == "rock") or (usrin == "sissor" and cp == "paper"):
        print("u win")
        usrw+=1
        continue

    elif usrin == cp:
        print("draw")
        continue
    

    else:
        print("u lose")
        usrw -= 1
        compwin +=1
        continue

if usrin == "quit":
        print(f"your score: {usrw}")
        if usrw < compwin:
            print("u win the game")
        elif usrw == compwin:
            print("draw match")
        else:
            print("u lose")
        
    


print("goodbye")
    





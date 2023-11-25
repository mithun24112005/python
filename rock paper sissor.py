import random
def play():
    usrw=0
    compw=0
    i=('r','s','p','q')
    while True:
        c=random.choice(['r','p','s'])
        ui=input("'r' for rock 'p' for paper 's' scissors and 'q' for quit: ").lower()
        if ui not in i:
            print("invalid input!!")
            break
        
        if ui==c:
            print("tie!!!")
        elif (ui=='r' and c=='s') or (ui=='s' and c=='p') or (ui=='p' and c=='r'):
            print("u won!!!")
            usrw+=1
        else:
            print("u lose!!!")
            compw+=1
        
        if ui=='q':
            print(f"your score= {usrw}")
            print(f"comp score= {compw}")
            print('finally u win!!') if usrw>compw else print("its a tie!!") if usrw==compw else print("u lose!! try again")
            break
play()


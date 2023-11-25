def sum(a,b,c):
    return a+b+c

def printboard(xs,zs):
    zero='X' if xs[0] else ('O' if zs[0] else 0)
    one='X' if xs[1] else ('O' if zs[1] else 1 )
    two='X' if xs[2] else ('O' if zs[2] else 2 )
    three='X' if xs[3] else ('O' if zs[3] else 3 )
    four='X' if xs[4] else ('O' if zs[4] else 4 )
    five='X' if xs[5] else ('O' if zs[5] else 5 )
    six='X' if xs[6] else ('O' if zs[6] else 6 )
    seven='x' if xs[7] else ('O' if zs[7] else 7 )
    eight='x' if xs[8] else ('O' if zs[8] else 8 )
    print(f" {zero} | {one} | {two} ")
    print(f"---|---|---")
    print(f" {three} | {four} | {five} ")
    print(f"---|---|---")
    print(f" {six} | {seven} | {eight} ")

def checkwin(xs,zs):
    xwins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6],[0,4,8],[2,4,6]]
    for win in xwins:
        if (sum(xs[win[0]],xs[win[1]],xs[win[2]])==3):
            print("X won the match")
            printboard(xs,zs)
            return 1
        if (sum(zs[win[0]],zs[win[1]],zs[win[2]])==3):
            print("O won the match!!")
            printboard(xs,zs)
            return 0
    return -1

xs=[0,0,0,0,0,0,0,0,0]
zs=[0,0,0,0,0,0,0,0,0]
turn=1 # 1 for X and 0 for O
print("welcome to tictactoe")

while True:
    printboard(xs,zs)
    if turn==1:
        print("X's turn")
        value=int(input("please enter a value: "))
        xs[value]=1
    else:
        print("O's turn")
        value=int(input("please enter a value: "))
        zs[value]=1
    cwin=checkwin(xs,zs)
    if cwin!=-1:
        print("match over")
        break
    turn=1-turn







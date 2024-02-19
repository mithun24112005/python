import random

def roll():
    min_val=1
    max_val=6
    roll=random.randint(min_val,max_val)
    return roll

while True:
    players=int(input("enter the number of players(2-4): "))
    if 2<=players<=4:
        break
    else :
        print("invalid enter again!")

max_score=50
p_score=[0 for _ in range(players)]

while max(p_score)<max_score:
    for p_idx in range(players):
        print(f"\nplayer number {p_idx+1} turn has started\n")
        print(f"your total score is: {p_score[p_idx]}\n")
        curr_score=0
        while True:
            should_roll=input("would you like to roll (y)?: ").lower()
            if should_roll!="y":
                break
            value=roll()
            if value==1:
                print("You rolled 1! Turn done!")
                curr_score=0
                break
            else:
                curr_score+=value
                print(f"you rolled a: {value}")
            print(f"your score is: {curr_score}")
        p_score[p_idx]+=curr_score
        print(f"the total score of player{p_idx+1} is: {p_score[p_idx]}")

max_score=max(p_score)
winning_idx=p_score.index(max_score)
print("player number",winning_idx+1, "is winner with score of: ",max_score)

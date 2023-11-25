import random
def guess(x):
    rn=random.randint(1,x)
    guess=0
    while guess!=rn:
        guess=int(input(f'guess a number bt 1 and {x}: '))
        print(guess)
        if guess<rn:
            print('sorry no is too low!')
        elif guess>rn:
            print('sorry no too high!')
    print("yay u have guessed right!!")
guess(10)
# rolling 2 dice and displaying the picture of them
# create dictionary that will hold the drawing of the dice

import random

def roll_dice():
    dice_drawing = {
        1: (
            "-----",
            "|   |",
            "| o |",
            "|   |",
            "-----",
        ),
        2: (
            "-----",
            "|o  |",
            "|   |",
            "|  o|",
            "-----",
        ),
        3: (
            "-----",
            "|o  |",
            "| o |",
            "|  o|",
            "-----",
        ),
        4: (
            "-----",
            "|o o|",
            "|   |",
            "|o o|",
            "-----",
        ),
        5: (
            "-----",
            "|o o|",
            "| o |",
            "|o o|",
            "-----",
        ),
        6: (
            "-----",
            "|o o|",
            "|o o|",
            "|o o|",
            "-----",
        ),}


    roll=input("Roll dice (YES/NO): ")
    while roll.lower()=="Yes".lower():
        d1=random.randint(1,6)
        d2=random.randint(1,6)
        print("dice rolled: {} and {}".format(d1,d2))
        print("\n".join(dice_drawing[d1]))
        print("\n".join(dice_drawing[d2]))
        roll=input("Roll again? (YES/NO): ")

roll_dice()


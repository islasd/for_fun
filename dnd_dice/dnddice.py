import random

totals = []

input("Welcome to the DND Character Creator Dice Roller!\nPress ENTER to begin rolling.")

for i in range (0,6): # create six stat numbers
    dice_rolls = []
    print(f"Roll Set {i+1}")
    for roll in range(0,4): # roll one dice 4 times (or four dice once if you want to view it that way)
        dice_no = random.randint(1,6)
        print(f"    Roll {roll + 1}: {dice_no}")
        dice_rolls.append(dice_no)

    sorted_dice_rolls = dice_rolls.copy()
    sorted_dice_rolls.sort()

    roll_of_lowest = dice_rolls.index(sorted_dice_rolls.pop(0)) # remove lowest dice roll
    print(f"Lowest roll was Roll {roll_of_lowest + 1}.")

    total = sum(sorted_dice_rolls) # add up the highest three dice rolls
    totals.append(total)
    print(f"Total of highest three rolls is {total}.\n")

for i, total in enumerate(totals):
    print(f"Total {i + 1}: {total}")

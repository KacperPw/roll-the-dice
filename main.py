import random


roll = input("Do you want roll the dice? \n Yes / No :")

if roll == "Yes":
    roll_dice = random.randrange(1, 6)
    print(roll_dice)
elif roll == "No":
    exit
else:
    print("Wprowadziłeś niepoprawną komendę")
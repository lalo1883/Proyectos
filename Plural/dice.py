import random

def roll():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

player_one = input("Type the name of player 1: ")
player_two = input("Type the name of player 2: ")

roll1 = roll() 
roll2 = roll() 

print(player_one, "rolled:", roll1)
print(player_two, "rolled:", roll2)

if roll1 > roll2:
    print(player_one,"won!!")
elif roll1 < roll2:
    print(player_two,"won!!")
else:
    print("It's a tied game.")



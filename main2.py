import random
'''
1 for snake
-1 for water
0 for gun
'''
priti = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

# Validate user input
if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}")
    print(f"Priti chose {reverseDict[priti]}")

    if priti == you:
        print("It's a draw!")
    elif (priti == -1 and you == 1) or (priti == 1 and you == 0) or (priti == 0 and you == -1):
        print("You win!\nAditya: oyaa 😁😁")
    else:
        print("You lose\npriti: Heee 😂😂")
    
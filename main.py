import random
'''
1 for snake
-1 for water
0 for gun
'''
priti = random.choice([-1, 0, 1])
youstr = input("enter your choice  ")
youDict = {"s": 1, "w": -1, "g": 0 }
reverseDict = {1: "snake", -1: "water", 0: "gun"}
you = youDict[youstr]

print(f"you chose {reverseDict[you]}\npriti choice is {reverseDict[priti]}")

if(priti == you):
    print("its a draw")

else:

 if(priti == -1 and you ==1):
    print("you win")

 elif(priti == -1 and you ==0):
    print("you lose")

 elif(priti == 1 and you ==-1):
    print("you lose ")

 elif(priti ==1 and you ==0):
    print("you win")

 elif(priti ==0 and you ==1):
    print("you win")

 elif(priti ==0 and you ==-1):
    print("you lose")

   
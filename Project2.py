import random
import time

def roll_dice():
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    total = n1 + n2
    print(n1, " + ", n2, " = ", total)
    return total

results = ["Win,Win!!!", "CRAPS!!!\nCasino Wins.", "You Lost."]
goal = roll_dice()
print("\n---------\nWe are going to roll a dice!\n---------\n")
time.sleep(1)

if goal == 7 or goal == 11:
    print(goal)
    time.sleep(1)
    print(results[0])
elif goal == 2 or goal == 3 or goal == 12:
    print(goal)
    time.sleep(1)
    print(results[1])
else:
    print("The Goal is ",goal,"\n-")
    while True:
        time.sleep(1)
        total = roll_dice()
        if total == goal:
            time.sleep(1)
            print("You've got the Goal! ")
            time.sleep(1)
            print(results[0])
            break
        elif total == 7:
            time.sleep(1)
            print(results[2])
            break
#the program is  written on windows powered visual studio code

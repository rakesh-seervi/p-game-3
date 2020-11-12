import random

you = int(input("Enter the runs from 1 to 10: "))
ran = random.randint(1, 10)
print(f"your run : {you}")
print(f"computer choose: {ran}")

while you != ran:
    you = int(input("Enter the runs from 1 to 10: "))
    ran = random.randint(1, 10)
    print(f"your run : {you}")
    print(f"computer choose: {ran}")
    
if you == ran :
    print("you are out")


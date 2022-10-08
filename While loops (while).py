# 1

first = 1
while first <= 1000:
    second = first % 3
    if second == 0:
        print(str(first))
        first = first + 1

# 2

l_inch = int(input("Enter the length in inches: "))
while l_inch >= 0:
    l_cm = round(l_inch * 2.54, 1)
    print(f"The length in cm is : {l_cm:.2f}")
    l_inch = int(input("Enter the length in inches: "))

# 3

largest_num = None
smallest_num = None
while True:
    number = input("Enter a number")
    if number == "":
        break
nums = []
while True:
    try:
        number = input("Enter a number: ")
        if number == "":
            break
        number = int(number)
        nums.append(number)
    except ValueError:
        print("Invalid input")
        break
print("Maximum number is", max(nums))
print("Minimum number is", min(nums))

# 4

import random
computer_integer = random.randint(1, 10)
player_integer = int(input("Guess the number from 1 to 10: "))
while player_integer != computer_integer:
    if player_integer >= computer_integer:
        print("Too high")
        if player_integer <= computer_integer:
            print("Too low")
            player_integer = int(input("Guess the number from 1 to 10: "))
            print("Correct")

# 5
tries = 0
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "python" and password == "rules":
    print("Welcome!")
elif tries == 0:
    while username != "python" and password != "rules":
        tries = tries + 1
        if tries == 5:
            print("Access denied")
            break

else:
    print("Try again")

# 6

import random
circle_points = 0
square_points = 0
Z = int(input("Enter a number of points: "))
while square_points != Z:
    square_points = square_points + 1
random_x = random.uniform(-1, 1)
random_y = random.uniform(-1, 1)
distance = random_x**2 + random_y**2
if distance < 1:
    circle_points = circle_points+1
pi = 4 * circle_points / square_points
print(pi)

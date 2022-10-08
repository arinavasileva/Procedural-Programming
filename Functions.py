import random

dice = 0
def roll():
    random_dice = random.randint(1, 6)
    return random_dice
while dice != 6:
    dice = roll()
    print(dice)

import random
dice = 0
def roll(sides):
    random_dice = random.randint(1, sides)
    return random_dice
sides = int(input("Tell me the number of sides:"))
while dice != sides:
    dice = roll(sides)
    print(dice)

def convert(gallons):
    litres = gallons * 3, 785411784
    return litres
gallons = float(input("Enter the quantity of gasoline in gallons:"))
while gallons >= 0:
    g = convert(gallons)
    print(str(gallons))
gallons = float(input("Quantity of gasoline in gallons is"))

def list_of_sum(i):
    s = 0
    for e in i:
        s += e
        return s


list_of_numbers = []
for number in range(10):
    list_of_numbers.append(random.randint(1, 10))
print(f"List of numbers is:"),
for i in range(len(list_of_numbers)):
    print(list_of_numbers[i], end="")
print(f"\n Sum is {sum(list_of_numbers)}")


import math
def pizza (diameter, price):
    return price / math.pi * (diameter / 200) ** 2
p1_d = float(input("Tell the d of the first pizza in cm:"))
p1_p = float(input("Tell the price of the first pizza in eu:"))
p2_d = float(input("Tell the d of the second pizza in cm:"))
p2_p = float(input("Tell the price of the second pizza in eu:"))
if pizza(p1_d, p1_p) < pizza(p2_d, p2_p):
    print("First pizza is better.")
else:
    print("Second pizza is better.")

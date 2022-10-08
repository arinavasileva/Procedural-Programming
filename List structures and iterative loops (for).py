import random
n = int(input("How many times to roll a dice?"))
dice_sum = 0
for i in range(n):
    dice = random.randint(1, 6)
    print(str(dice), end="")
    dice_sum = dice_sum + dice
print(f"\n The sum of the dices is: {dice_sum}")

numbers = []
prompt = "Give me a number?"
s = input(prompt)
while s != "":
    numbers.append(float(s))
    s = input(prompt)
numbers.sort(reverse=True)
print(numbers[0:min(5, len(numbers))])

import math
n = int(input("Give the number?"))
for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
        print(f"Dividable by {i}")
        break
else:
    print("It is a prime number")

cities = []
for n in range(s):
    cities.append(input("Give me the name of the cities"))
for city in cities:
    print(cities)

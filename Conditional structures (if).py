# 1

zander = float(input('Enter the length of a zander in centimeters:'))
if zander < 42:
    print("Release the fish back into the lake.")
print(f"The caught fish was {42 - zander:.1f} cm below the size limit")


# 2

cabin_class = input("Enter the cabin class of a cruise ship (LUX, A, B or C): ")
if cabin_class == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin_class == 'A':
    print('Above the car deck, equipped with a window.')
elif cabin_class == 'B':
    print("Windowless cabin above the car deck.")
elif cabin_class == 'C':
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")


# 3

p_gen = input('Enter your biological gender (Female or Male):')
p_gem = int(input('Enter your hemoglobin value in g/l:'))
if p_gen == "Female":
    if 117 <= p_gem <= 155:
        print("Hemoglobin value is normal")
    elif p_gem < 117:
        print("Hemoglobin value is low.")
    elif p_gem > 155:
        print("Hemoglobin value is high.")
if p_gen == "Male":
    if 134 <= p_gem <= 167:
        print("Hemoglobin value is normal")
    elif p_gem < 134:
        print("Hemoglobin value is low.")
    elif p_gem > 167:
        print("Hemoglobin value is high.")


# 4

year = int(input('Enter a year:'))
y1 = year % 4
y2 = year % 100
y3 = year % 400
if y1 == 0:
    if y2 == 0 and y3 != 400:
        print("The input year is not a leap year")
else:
    print("The input year is a leap year.")




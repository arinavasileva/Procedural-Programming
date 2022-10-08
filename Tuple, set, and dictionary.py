# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

seasons_of_the_year = ("spring", "summer", "autumn", "winter")
month_number = int(input("Enter the number of the month(1-12):"))
if month_number in (1, 2, 3):
    print("Season is winter")
elif month_number in (4, 5, 6):
    print("Season is spring")
elif month_number in (7, 8, 9):
    print("Season is summer")
else:
    print("Season is autumn")

# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending
# on whether the name was entered for the first time. Finally, the program lists out the input
# names one by one, one below another in any order. Use the set data structure to store the names.

names_list = set()
names = input("Enter the name:")
while names != "":
    new_name = len(names_list)
    names_list.add(str(names))
    existing_name = len(names_list)
    if new_name < existing_name:
        print("New name")
    else:
        print("Existing name")
    names = input("Enter the name:")
    for x in names_list:
        print(x)



# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks
# the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit,
# the program execution ends. The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport
# is EFHK. You can easily find the ICAO codes of different airports online.)

airport_name = {"Zaporizhzhia International Airport": "UKDE",
                        "Venice Marco Polo Airport": "LIPZ",
                        "Rotterdam The Hague Airport": "EHRD"}
print(airport_name)

dictionary = {}
print("Type new to enter new airport")
print("Type f to fetch information of existing airport")
print("Type q to quit")
c = str(input("What should the program do?:"))
while c != "q":
    if c == "new":
        print("Input the ICAO code and choose the airport")
        code = str(input("ICAO code: "))
        airport_name = str(input("Airport Name: "))
        dictionary[code] = airport_name
    elif c == "f":
        print("Input the ICAO code to find the airport")
        code = str(input("ICAO code: "))
        print(dictionary[code])
    else:
        print("No available information")
    c = str(input("What should the program do?:"))






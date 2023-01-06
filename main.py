# This is a roller coaster ticketing machine. Assignment one
# print("Welcome to the roller coaster machine!")
# height = int(input("What is your height? (in cm) "))
# if height >= 120:
#     print("You can ride the roller coaster!")
# else:
#     print("Sorry you have to grow taller before you can ride.")

# Coding exercise 1
# userNumber = int(input("Type down any number: "))
# checkNumber = userNumber % 2
# if checkNumber != 0:
#     print("Your input is an odd number.")
# else:
#     print("Your input is an even number")

# Nested conditional statements
customerHeight = int(input("What is your height? (in cm) "))
if customerHeight >= 120:
    print("You will ride the roller coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ride will cost $5")
    elif age <= 18:
        print("Your ride will cost only $7")
    elif age > 18:
        print("Your ride will cost only $12")
else:
    print("Sorry, you have to grow taller before you can ride. ")

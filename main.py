# Roller coaster ticketing application _ Revision (Best Version!)
print("Welcome to Securepoint Roller Coaster!")
height = int(input("Please input your height (in cm): "))
if height >= 120:
    print("You can experience the epic ride of Securepoint Roller Coaster!")
    age = int(input("How old are you? "))
    if age <= 7:
        print("Your bill will be $10")
    elif age <= 15:
        print("Your bill will be $20")
    elif age < 18:
        print("Your bill  will be $25")
    elif age >= 18:
        print("Your bill will be $30")
else:
    print("Sorry. For your safety, you cannot ride the roller coaster. Please come back when you've grown taller")




























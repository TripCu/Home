from datetime import datetime
import re
print("Welcome to Date and Time inc just ask for the date or the time")
current_datetime = datetime.now()

def menu ():
    print("[1] Date")
    print("[2] Time")
    print("[0] Exit the program")


menu()
option = int(input("Enter your option:  "))

while option != 0:
    if option == 1:
        print("Current date:", current_datetime.date()) 
        print("Current day:", current_datetime.strftime("%A"))
        print("Current year:", current_datetime.year)
    elif option == 2:
        print("Current time:", current_datetime.time())
        military_time = datetime.now().time()
        standard_time = military_time.strftime("%I:%M %p")
        print("Standard time:",standard_time)
    else:
        print("invalid option.")

    print()
    menu()
    option + int(input("Enter your option;"))

print("Thanks for using this program today       Goodbye.")
# Merab Tsitskhvaia

height = int(input("Enter your weight in cm: "))
choice = input("Enter cm or foot: ")

if choice == "cm":
    print("Your height is " + str(height) + " cm")
elif choice == "foot":
    print("Your height is " + str(height / 30.48) + " foot")
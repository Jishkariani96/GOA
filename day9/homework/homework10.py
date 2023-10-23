# Nino Goglichadze

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

   
if a + b > c and a + c > b and b + c > a:
    perimeter = a + b + c
    print("ამ სამკუთხედის პერიმეტრია" + str(perimeter))
else:
    print("ასეთი სამკუთხედი არარსებობს.")
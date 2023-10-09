name = input("Enter your name: ")
age = int(input("Enter your age: "))
year = 2023
for i in range(10):
    age += 1
    year += 1
    print(name + " you will be " + str(age) + " years old at " + str(year))
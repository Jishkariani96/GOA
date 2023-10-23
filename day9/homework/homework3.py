# Rati Murgulia

name1 = input("Enter first name: ")
name2 = input("Enter second name: ")

a1 = 0
a2 = 0

for char in name1:
    if char in "Aa":
        a1 += 1
for char in name2:
    if char in "Aa":
        a2 += 1

if a1 > a2:
    print("First name contains more 'A' letters")
elif a2 > a1:
    print("Second name contains more 'A' letters")
else:
    print("Its Equal")


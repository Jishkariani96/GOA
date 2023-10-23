# Nino Solomonia

Group4 = []
counter = 0
for i in range(22):
    Group4.append(input("Enter student's full name: "))

for element in Group4:
    for char in element:
        if char in "AaIi":
            counter += 1
print("Answer is " + str(counter))











# Tsotne Sartania
wrong = 0

question1 = int(input("5 + 2 = :"))
if question1 != 7:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question2 = int(input("2 * 4 = :"))
if question2 != 8:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question3 = int(input("24 / 4 = :"))
if question3 != 6:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question4 = int(input("78 - 20 = :"))
if question4 != 58:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question5 = int(input("33 / 3 = :"))
if question5 != 11:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question6 = int(input("57 + 13 = :"))
if question6 != 70:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question7 = int(input("4 * 4 = :"))
if question7 != 16:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question8 = int(input("66 + 66 = :"))
if question8 != 132:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

question9 = int(input("12 * 3 = :"))
if question9 != 36:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")
    
question10 = int(input("39 + 11 = :"))
if question10 != 50:
    wrong += 1
    print("wrong answer!")
else:
    print("Correct!")

if wrong > 0:
    print("კიდევ სცადეთ ან შემოგვიერთდი GOA ში, GOA ელს ეს არეკადრება:")
else:
    print("შენ აშკარად GOA ში სწავლობდი ჩემო ძმ(დ)აო")
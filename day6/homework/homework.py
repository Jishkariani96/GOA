score = int(input("Enter your score: "))
score_2 = int(input("Enter your second score: "))
score_3 = int(input("Enter your third score: "))

x = (score + score_2 + score_3) / 3

if x > 9:
    print('გილოცავთ მატრიცელო, შენ გადმოგეცა 300 ლარიანი ბანძი ტოსტერი რასაც შეალიე შენი ცხოვრების წლები')
elif x < 5:
    print("გილოცავ, შენ გაექეცი მატრიცას")
elif x > 5 and x < 9:
    print("YOU ARE MID!")
if x < 0 or x > 10:
    print("There's something wrong with you")







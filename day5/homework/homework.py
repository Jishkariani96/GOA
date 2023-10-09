# Comparison of father and kids ages:
user_age = int(input("Enter your age: "))
user_fathers_age = int(input("Enter your fathers age: "))

for i in range(10):
   user_age += 1
   user_fathers_age += 1
   print("After a year your dad will be older as : " + str(user_fathers_age // user_age))
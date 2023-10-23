# Luka Kechexmadze 

price = int(input("Enter your price: "))

discount = (price - (price / 100 * 10))
profit = discount / 100 * 8
old_profit = price / 100 * 8

print("Seller would had " + str(discount * (old_profit - profit) / 100) + " % profit")


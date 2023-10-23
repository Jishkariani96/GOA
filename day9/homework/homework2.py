#Luka Siradze

word = input("Enter your word: ")

cons = 0

for char in word:
    if char not in "aeiou":
        cons += 1
print("Your word has " + str(cons) + " cons")

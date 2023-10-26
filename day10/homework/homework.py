import random 


arr = ["Giorgi Chkhetiani", "Beqa Giorgobiani", "Luka Chkhitunidze","Rati Murghulia", "Saba Vakhtangadze", "Giorgi Lobjanidze", "Nini Goglichadze","Salome Miladze","Nino Solomonia","Tsotne Sartania","Merab Tsitskhvaia","Tsotne Kevkhishvili"]
scores = []
x = 0
for i in range(len(arr)):
    called = random.choice(arr)
    print(called,"Dafastan tu sheidzleba!")
    arr.remove(called)
    answer = input("did the student answer correctly: ")
    if answer == "yes":
        scores.append(called +  " " +str(x + 10))
    elif answer == "no":
        scores.append(called + " " + str(x - 5))
    print(scores)
                    



    

# პაროლის დაგენერირება

import random

password = ""

nums = [0,1,2,3,4,5,6,7,8,9]
simbols = "!@#$%^&*_-"
alphabets = "abcdefghijklmnopurstuvwxyz"


for i in range(2):
    password += str(alphabets[random.randint(0,len(alphabets) -1)])

for i in range(2):
    password += str(simbols[random.randint(0,len(simbols)-1)])

for i in range(4):
    password += str(nums[random.randint(0,8)])    

print("new password is:",password)





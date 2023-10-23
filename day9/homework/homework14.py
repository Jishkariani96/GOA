# Beqa Giorgobiani

arr = [21, -3, 11, -31, 7, -34]

arr.insert(5, int(input("Enter your num: ")))
print(arr)

sum = 0
for num in arr:
    if num > 0:
        sum += num

print(sum)
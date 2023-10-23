# Giorgi Chkhetiani

my_list = [input("str goes here: "), input("Another str: "), input("And another: ")]

min = my_list[0]
mid = ""
max = my_list[0]

for element in my_list:
    if len(min) > len(element):
        min = element
for element in my_list:
    max = element
    if len(max) < len(element):
        max = element
for element in my_list:
    if element != min and element != min:
        mid = element
print(mid)

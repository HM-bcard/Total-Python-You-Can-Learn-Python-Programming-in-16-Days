number = 10

while number >= 0:
    print(number)
    number -= 1

# 2

number = 50

while number >= 0:
    if number % 5 == 0:
        print(number)
        number -= 1
    else:
        number -= 1

# 3

list_numbers = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for number in list_numbers:
    if number < 0:
        break
    else:
        print(number)
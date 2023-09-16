# 1

students = ["Norville", "Fred", "Velma", "Daphne"]

for student in students:
    print(f"Hello {student}")

# 2

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]


sum_numbers = 0

for number in list_numbers:
    sum_numbers += number
print(sum_numbers)

# 3

list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

sum_even = 0

sum_odd = 0

for number in list_numbers:
    if number % 2 == 0:
        sum_even += number
    else:
        sum_odd += number
print (sum_even)
print (sum_odd)
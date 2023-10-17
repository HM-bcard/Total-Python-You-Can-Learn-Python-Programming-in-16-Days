def check_4_digits(number):
    return number in range(999, 10000)

sum = 999 + 12
result = check_4_digits(sum)
print(result)
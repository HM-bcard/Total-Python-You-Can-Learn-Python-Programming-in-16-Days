#  1

values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = [a ** 2 for a in values]


# 2

values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [a for a in values if a % 2 == 0]
print(even_values)


# 3

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(temp - 32) * (5/9) for temp in temperature_fahrenheit]
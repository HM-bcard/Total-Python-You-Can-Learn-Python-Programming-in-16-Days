var_1 = True
var_2 = False
print(type(var_1))
print(var_1)

number = 5 > 2 + 3
print(type(number))
print(number)


number = 5 >= 2 + 3
print(type(number))
print(number)

number = bool(5 < 6)  # putting an expression directly
print(type(number))
print(number)


list1 = [1, 2, 3, 4]
control = 5
print(type(control))
print(control)

list1 = [1, 2, 3, 4]
control = 5 not in list1
print(type(control))
print(control)

def check_3_digits(number):
    return number in range(100, 1000)


sum = 526 + 311
result = check_3_digits(sum)
print(result)


def check_3_digits(list1):
    for number in list1:
        if number in range(100, 1000):
            return True
        else:
            pass


sum = 526 + 311
# result = check_3_digits(sum)
print(result)


def check_3_digits(list1):
    for number in list1:
        if number in range(100, 1000):
            return  True # return true kills a function
        else:
            pass


result = check_3_digits([55, 99, 6000])
print(type(result))


def check_3_digits(list1):
    for number in list1:
        if number in range(100, 1000):
            return True # return true kills a
        else:
            pass
    return False


result = check_3_digits([55, 99, 600])
print(type(result))
print(result)


def check_3_digits(list1):

    three_digits_list = []

    for number in list1:
        if number in range(100, 1000):
            three_digits_list.append(number)
        else:
            pass
    return three_digits_list


result = check_3_digits([55, 99, 600])
print(type(result))
print(result)
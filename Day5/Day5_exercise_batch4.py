# 1

def all_positives(list1):
    for n in list1:
        if n < 0:
            return False
        else:
            pass
    return True


numbers = [-1, 0, 2, 3]

# 2

def sum_less(list1):
    sum_n = 0.
    for n in list1:
        if n > 0 and n < 1000:
            sum_n += n
        else:
            pass
    return sum_n


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1000]


# 3


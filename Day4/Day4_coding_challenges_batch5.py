list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
my_tuples = list(enumerate(list_names))

for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')



# 2

string = "Python"

list_string = list(string)

tuples_string = enumerate(list_string)

indices_list = list(tuples_string)

print(indices_list)


for index, name in enumerate(list_string):
    print(f'{name} is found at index {index}')

# 3


list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]


for index, name in enumerate(list_names):
    # print(index, name)
    if 'M' == name[0]:
        print(index)
    else:
        continue

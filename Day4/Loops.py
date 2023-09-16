names = ['John', ]

my_list = ['a', 'b', 'c', 'd']

for lettter in my_list:  # right click refactor
    print(lettter)

for a in [1, 2, 3]:
    print(a + 1)

for dinosaur in my_list:
    print(dinosaur)

for letter in my_list:
    letter_number = my_list.index(letter) + 1
    print(f"letter {letter_number}: {letter}")

my_list = ['Paul', 'Laura', 'Fede', 'Louis', 'laundry']

for name in my_list:
    if name.startswith('L') or name.startswith('l'):
        print(name)
    else:
        print("No L\'s")


numbers = [1, 2, 3, 4, 5]
my_value = 0

for n in numbers:
    my_value = my_value + n
print(my_value)

for n in numbers:
    my_value = my_value + n
print(my_value)

for n in numbers:
    my_value = my_value + n
    print(my_value)

word = 'python'

for l in 'python':
    print(l)


for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)


print("\n")

dic = {'key1': 'a', 'key2': 'b', 'key3': 'c'}

for item in dic.values():
    print(item)


dic = {'key1': 'a', 'key2': 'b', 'key3': 'c'}

for a, b in dic.items():
    print(a, b)

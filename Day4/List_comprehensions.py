word = 'python'
my_list = [letter for letter in word]
print(my_list)

word = input('saskatchewan?:')
my_list = [a * 2 for a in word]
print(my_list)

word = 'python'
my_list = []

for letter in word:
    my_list.append(letter)

print(my_list)

my_list = [a for a in 'bottomless crocodile']

print(my_list)

my_list = [n / 2 for n in range(0, 21, 2)]

print(my_list)


my_list = [n for n in range(0, 21, 2) if n * 2 > 10]

print(my_list)


feet = [10, 20, 30, 40, 50]
meters = [foot / 3.28084   for foot in feet]
print(meters)



my_list = ['a', 'b', 'c']
index = 0

for item in my_list:
    print(index, item)
    index += 1

for item in enumerate(my_list):
    print(item)


for index, item in enumerate(my_list):
    print(index, item)

for index, item in enumerate(range(50, 55)):
    print(index + 1, item)


my_list = ['a', 'b', 'c']

my_tuples = list(enumerate(my_list))
print(my_tuples)
print(my_tuples[0][0])
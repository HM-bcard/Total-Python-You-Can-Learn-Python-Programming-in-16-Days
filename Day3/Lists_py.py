my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[0]
print(result)

my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[0:-1]
print(result)

my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[0:]
print(result)

my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[-2:]
print(result)

my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[-1:]
print(result)

my_list = ['a', 'b', 'c']
# can contain diff data types
result = my_list[-1]
print(result)

my_list = ['1', '2', '3']
my_list2 = ['a', 'b', 'c']
my_list3 = my_list + my_list2
print(my_list3)

my_list3[0] = 'alpha'

my_list = ['1', '2', '3']
my_list2 = ['a', 'b', 'c']
my_list3 = my_list + my_list2
my_list3.append('g')
my_list3.pop()  # deletes the last element on a list
print(my_list3)

my_list = ['1', '2', '3']
my_list2 = ['a', 'b', 'c']
my_list3 = my_list + my_list2
my_list3.append('g')
my_list3.pop(0)  # deletes the selected element on a list
print(my_list3)

list1 = ['g', 'd', 'r', '1', 'a', 'h']
list1.sort()
print(list1)

list1 = ['g', 'd', 'r', '1', 'a', 'h']
new_list = list1.sort()  # doesn't store it(the list)
print(list1)
print(type(list1))
print(new_list)

# None is an object that doesn't return anything

list1 = ['g', 'd', 'r', '1', 'a', 'h']
new_list = list1.reverse()  # doesn't store it(the list)
print(list1)
print(type(list1))
print(new_list)
my_dict = {'c1': 'value1', 'c2': 'value1'}
print(type(my_dict))
print(my_dict)

# key cannot be repeated, value can be repeated

my_dict = {'c1': 'value1', 'c2': 'value1'}
# print(my_dictionary)

customer = {'name': 'John', 'last_name': 'Lennon', 'weight':88, 'height': 1.76}
query = (customer['last_name'])

print(query)

dic = {1: 55, 2: [10, 20, 30], 3: {'s1': 100, 's2': 200, 3: 666}}
print(dic[3])
print(dic[3][3])

dic = {'k1': ['a', 'b', 'c'], 'k2': ['d', 'e', 'f']}
print(dic['k2'][1].upper())
# hehehehehe :)

# new dict value:

dic[3] = 'c'
print(dic)

dic[2] = 'c'
print(dic)

print(dic.keys())

print(dic.values())

print(dic.get(1))


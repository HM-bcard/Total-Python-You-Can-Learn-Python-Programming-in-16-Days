# set1 = set(1, 2, 3, 4, 5, 6) needs one argument

set2 = {1, 2, 3, 4, 5, 6}

# same sets ^

# python discards the duplicate values in sets
# they are immutable
# you cannot store lists and dictionaries

my_set = set([1, 2, 3, 4, 5])
print(type(my_set))
# print(type(set1))
print(type(set2))
print(my_set)
#  print(set1)
print(set2)

my_set = set((1, 2, 3, 4, 5))
print(type(my_set))


s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.remove(3)
print(s1)

s1.pop() # in sets pop removes a random element
print(s1)

s1.clear()
print(s1)

s1.add(3)
print(s1)
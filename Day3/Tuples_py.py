my_tuple = ('a','b','c')
print(my_tuple)
#  tuples take up less memory
my_tuple = 1,2,3,4
print(my_tuple)

print(my_tuple[0])

my_tuple = 1,2,(1,10),3,4
print(my_tuple)

print(my_tuple[2][0])

my_tuple = 1,2,(1,10),3,4

my_tuple = list(my_tuple)

my_tuple = tuple(my_tuple)

print(my_tuple)

# immutable doesn't influence type casting

t = (1, 2, 3)

x, y, z = t

print(x, y, z)

#  x,y = t

#  e,r,f,t = t

t = 1, 2, 3, 4

print(t.count(1))  # counts occurrences of one
print(t.index(2))  # shows the index of the querying value
print(t)


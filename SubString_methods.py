# slicing

my_var = 'text'

my_var = my_var[1:2]

print(my_var)

# examples

text = 'ABCDEFGHIJKLM'
fragment = text[2:6]
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[2:]
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[:6]
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[2:11:2]
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[::]
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[-10:-2:-2]  # reverse order
print(fragment)


text = 'ABCDEFGHIJKLM'
fragment = text[::-2]  # reverse order
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[3::-2]  # reverse order
print(fragment)

text = 'ABCDEFGHIJKLM'
fragment = text[:8:-2]  # reverse order
print(fragment)


text = 'ABCDEFGHIJKLM'
fragment = text[-8:-1:-1]  # reverse order
print(fragment)





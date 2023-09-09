my_text = 'This text is a text'
result = my_text[0]
print(result)
result = my_text.index('h')
print(result)
result = my_text.index('text')
print(result)
# index is case sensitive

result = my_text.index('s') #only the first result
print(result)

result = my_text.index('s', 5)
print(result)

result = my_text.rindex('s')
print(result)
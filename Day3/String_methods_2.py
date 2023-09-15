# :
# upper()
'''
print('comment')
upper()
lower()
split()
join()
find()
-> there are 30 string methods
'''


text = "We are going to learn six methods today"
result = text.upper()
print(result)


text = "We are going to learn six methods today"
result = text.upper
print(result)


text = "We are going to learn six methods today"
result = text.lower()
print(result)


text = "We are going to learn six methods today"
result = text.split()
print(result)


text = "We are going to learn six methods today"
result = text.split('o')
print(result)


text = "We are going to learn six methods today"
result = text.split()
print(result)

a = 'learning'
b = 'python'
c = 'is'
d = 'amazing'

e = " ".join([a,b,c,d])

print(e)

text = "We are going to learn six methods today"
result = text.split()
print(result)

a = 'learning'
b = 'python'
c = 'is'
d = 'amazing'

e = "-".join([a,b,c,d])

print(e)

# input()

text = "We are going to learn six methods today"
result = text.find('t')
print(result)


text = "We are going to learn six methods today"
result = text.replace('t','666')
print(result)


text = 'If the implementation is hard to explain, it might be a bad idea.'
text_replaced1 = text.replace('hard','easy')
text_replaced2 = text_replaced1('bad','good')
print(text_replaced2)

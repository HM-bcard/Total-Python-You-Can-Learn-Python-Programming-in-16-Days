from random import *  # press control + space bar, * - import all inside
#  from random import randint
my_random = randint(1, 50)
print(my_random)

my_random = uniform(1, 5)
print(my_random)

my_random = round(uniform(1, 5), 1)
print(my_random)

my_random = round(uniform(1, 5), 1)
print(my_random)

my_random = random()  # random float between zero and one
print(my_random)

# choice

colours = ['red', 'blue', 'black', 'yellow', 'brown']
my_random = choice(colours)
print(my_random)

numbers = list(range(5, 50, 5))
print(numbers)
shuffle(numbers)  # in-place method, it changes the string
print(numbers)






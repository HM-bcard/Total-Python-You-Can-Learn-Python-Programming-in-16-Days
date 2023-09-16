coins = 5

# while coins > 0:
    # print(f"I have {coins} coins")


answer = 'y'

while answer == 'y':
    answer = input('do you want to continue y/n?')
else:
    print('Thank you')

    # pass
    # break
    #  continue

answer = 'y'

while answer == 'y':
    answer = input('do you want to continue y/n?')
else:
    print('Thank you')

name = input("Your name")

for letter in name:
    if letter not in name:
        pass
    else:
        print(letter)

print('\n')

for letter in name:
    if letter == 'r':
        break
    print(letter)


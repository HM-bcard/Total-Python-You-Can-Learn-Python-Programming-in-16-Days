coffee_prices = [('cappuccino', 1.5),
                 ('espresso', 1.91),
                 ('mocha', 1.9)]
'''
for coffee, price in coffee_prices:
    print(coffee)
'''

def most_expensive_coffee(list_of_prices):

    highest_price = 0
    my_most_expensive_coffee = ''

    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price = price
            my_most_expensive_coffee = coffee
        else:
            pass

    return(my_most_expensive_coffee, highest_price)

print(most_expensive_coffee((coffee_prices)))

coffee, price = most_expensive_coffee(coffee_prices)

print(f'The most expensive coffee is {coffee}, whose price is {price}')
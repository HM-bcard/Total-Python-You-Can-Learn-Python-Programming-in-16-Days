# 1

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

combo = list(zip(capitals,countries))

for capyital, country in combo:
    print(f"The capital of {country} is {capyital}")

# 2

brands = ['My brand', 'My brand also', 'My third brand']
products = ['Product1','Product2','Product3']

# my_zip = list(zip(brands, products)) - not a list

brands = ['My brand', 'My brand also', 'My third brand']
products = ['Product1', 'Product2', 'Product3']

my_zip = zip(brands, products)
print(my_zip)[1]

# 3


spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

translations_zip = zip(spanish, portuguese, english)
numbers = list(translations_zip)

my_list = [1, 2, 2, 3]

cartons_of_milk = ['carton', 'carton', 'carton', 'carton']

cartons_of = list(zip(my_list, cartons_of_milk))
print(cartons_of)

names = ['Hanna']

names = ['Hanna', 'Bruce', 'Tony']
ages = [65, 29, 42, 55]
cities = ['New York', 'London', 'Berlin']

combination = list(zip(names, ages, cities))

print(combination)

for name, b, city in combination:
    print(f"{name} is {b} years old, and lives in {city}")


for a, b, city in combination:
    print(f"{a} is {b} years old, and lives in {city}")


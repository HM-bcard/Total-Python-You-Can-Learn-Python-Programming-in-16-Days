from random import *
series = choice(["N-01","N-02","N-03","Random"])

if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("This product doesn\'t exist")


series = choice(["N-01", "N-02", "N-03", "Random"])
# match
'''if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("This product doesn\'t exist")
'''

series = choice(["N-01", "N-02", "N-03", "Random"])
match series:
    case  "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("This product doesn\'t exist")


client = {'name': 'Federico',
          'age': 46,
          'occupation': 'online instructor'}

movie = {'title': 'Matrix',
         'credits': {'main_star': 'Keanu Reeves',
                     'director': 'Lana & Lily Wachowski'}}

items = [client, movie, 'book']


for i in items:
    match i:
        case{'name': name,
             'age': age,
             'occupation': occupation}:
            print('It is a client')
            print(name, age, occupation)
        case {'title': title,
              'credits': {'main_star': main_star,
                          'director': director}}:
            print('This is a movie')
            print(title, main_star, director)
        case _:
            print("I don't know what this is")


    def func(x):
        if x == 0:
            return 0
        return x + func(x - 1)


    print(func(3))
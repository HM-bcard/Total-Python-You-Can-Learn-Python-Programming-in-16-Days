# Challenge 1

input1 = input("Please enter text here: ")
letter_1 = input("Please enter a random letter")
letter_2 = input("Please enter a second random letter:")
letter_3 = input("Please enter a random third letter:")

list_of_letters = [letter_1, letter_2, letter_3]

print(f"""The first letter appears {(input1.count(letter_1) + input1.count(letter_1.upper()))} times 
the second letter appears {(input1.count(letter_2) + input1.count(letter_2.upper()))} times
the third letter appears {(input1.count(letter_3) + input1.count(letter_3.upper()))} times""")


#  Challenge 2
Challenge_2 = (len(input1.split()))
print(Challenge_2)

# Challenge 3

print(input1[0])
print(f"The first letter is '{input1[-1]}' ")


# Challenge 4 Reversing list

Challenge_4_interim = input1.split()
print(Challenge_4_interim.reverse())
Challenge_4 = " ".join(Challenge_4_interim)
print(Challenge_4)

# Challenge 5

Is_there_a_python = input1
print("python" in Is_there_a_python)



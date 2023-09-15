text = input("Enter a text of your choice: ")
letters = []

text1 = text.lower()  # to check in a case-insensitive manner

letters.append(input("Please enter a random letter").lower())  # lowering the letter case in order to check the text \n
# input
letters.append(input("Please enter a second random letter").lower())
letters.append(input("Please enter a third random letter").lower())


print("\n")
print("LETTER REPETITIONS:")

letter_repetition1 = text1.count(letters[0])
letter_repetition2 = text1.count(letters[1])
letter_repetition3 = text1.count(letters[2])

print(f"We found the letter '{letters[0]}'repeated {letter_repetition1} times ")
print(f"We found the letter '{letters[1]}'repeated {letter_repetition2} times ")
print(f"We found the letter '{letters[2]}'repeated {letter_repetition3} times ")

# challenge 2

print("\n")
print("NUMBER OF WORDS")

words = text.split()
print(f"We have found {len(words)} words in your text")

print("\n")
print("First and last letters are:")

first_letter: str = text[0]  # use 'text' var to check for the user provided letter(case-sensitive)
last_letter = text[-1]
print(f"The initial letter is {first_letter}, the final letter is {last_letter}")

print("\n")
print("INVERTED TEXT")

words.reverse()
inverted_text = ' '.join(words)
print(f"Your input text in reverse is: {inverted_text}")

print("\n")
print("LOOKING FOR PYTHON")

is_python = 'python' in text
dic = {True: "was", False: "was not"}

print(f"The word 'Python' {dic[is_python]} found in the text")




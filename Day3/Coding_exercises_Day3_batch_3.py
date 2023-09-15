sentence = "Especially in electronic communications, writing in all caps is equivalent to yelling."
print(sentence.upper())

# exercise_2

word_list = ["Simple","is","better","than","complex."]
word_list = " ".join(["Simple","is","better","than","complex."])
# word_list = str(word_list)
print(word_list)

word_list = ["Simple","is","better","than","complex."]
word_list = str(word_list)
word_list = " ".join(["Simple","is","better","than","complex."])
word_list = str(word_list)
print(word_list)

text = 'If the implementation is hard to explain, it might be a bad idea.'
text_replaced1 = text.replace('hard','easy')
text_replaced2 = text_replaced1.replace('bad','good')
print(text_replaced2)
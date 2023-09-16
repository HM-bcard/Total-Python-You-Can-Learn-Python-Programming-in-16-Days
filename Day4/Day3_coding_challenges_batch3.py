# 1

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

if num1 > num2:  # 'If' is case-sensitive
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")

# 2

age = 16
has_license = False

if age == 18 and has_license == true:
    print("You can drive")
elif age < 18 and has_license == False:
    print("You can't drive yet. You must be 18 years old and have a license")
else:
    print("You can't drive. You need to have a license")

#  3

speak_french = True
knows_python = False

if speak_french == True and knows_python == True:
    print("You meet the requirements to apply")
elif speak_french != True and knows_python != True:
    print("To apply, you need to know how to program in Python and speak French")
elif speak_french != True and knows_python  == True:
    print("To apply, you need to speak French")
else:
    print("To apply, you need to know how to program in Python")


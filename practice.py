'''For loops'''
# for number in range(1,10,2):
#    print ("Attempt", number , (number ) * ".", "imtiaz")

'''For else loop'''
#successful = True
# for number in range(3):
#    print("Attempt")
#    if successful:
#        print("Successful")
# else:
#    print("Attempted 3 times and failed")


'''Nested Loops'''

# for x in range (5):
#    for y in range(3):
#        print(f"({x}, {y})")

'''Iterables'''
# print(type(5))
# print(type(range(5)))
# for x in range(5):
#    print('imtiaz')
# for x in "Python":
#    print(x)
# for x in [1,2,3,4]:
#    print(x)

'''While Loops'''
# While loop is used to run something/iterate over iterable objects as long as the condition is true

#number = 100
# while number > 0:
#    print(number)
#    number = number // 2
#    #number //= 2

#command = ""
#while command.lower() != "quit":   """This is the better code than the below"""
# while command != "quit" and  command != "QUIT":
#    command = input(">>")
#    print("ECHO", command)


'''Infinite Loops'''
# while True:
#    command = input('>')
#    print("ECHO", command)
#    if command.lower() == 'quit':
#        break

# print(ord("g"))

'''Conditional Statements'''

#temperature = 17
# if temperature > 30:
#    print('it is warm')
#    print("Drink water")
# elif temperature < 15:
#    print("it's cold")
#else:#
#    print("It is nice weather")
# print("Done")

'''Ternary Operator'''
#age = 12
# if age >=18:
#    print("Eligible")
# else:
#    print("Not eligible")

# A slight better code
#age = 20
# if age >= 18:
#    message ="Eligible"
# else:
#    message = "Not eligible"
# print(message)

# The best code/Ternary code
#age = 21
#message = "Eligible" if age >= 18 else "Not eligible"
# print(message)

'''Logical Operators'''
# and or not

#high_income = False
#good_credit = True
#student = False

# if high_income and good_credit:
#    print("Eligible")
# else:
#    print('Not eligible')

# if (high_income or good_credit) and not student:
#    print("Eligible")
# else:
#    print("Not eligible")


'''Short-circuit Evaluation'''
#high_income = True
#good_credit = True
#student = True

# if(high_income and good_credit) and not student:
#    print("Eligible")
# else:
#    print("Not eligible")

'''Quiz'''

#if 10 == '10':
#    print('a')
#elif 'bag' > 'apple' and 'bag' > 'cat':
#    print('b')
#else:
#    print('c')

'''Strings'''

# course = "Python Programming"
# print(len(course)) # Print the length of the string
# print(course[0])  #Print the first character of the string
# print(course[-1]) #Print the rightmost character
# print(course[0:3]) # Print the first 3 characters 0,1,2
# print(course[:3])  # Print the first 3 characters 0,1,2
# print(course[0:])  # Print the whole string from the beginning to the end
# print(course[:])  # Print the whole string from the beginning to the end

'''Escape Sequence'''
#\"
#\'
#\\
#\n              this will create a newline

# course = "Python \'Programming'"
# print(course)

# course = "Python \nProgramming"
# print(course)

''' Formatted Strings'''

# first = "Imtiaz"
# last = "Ahmed"
# # full = first + " " + last
# #full = f"{first} {last}"
# full = f"{len(first)}{last}"
# print(full)

""" String Methods"""

# course = "  Python programming"
# print(course)
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())  # Removes white spaces
# print(course.lstrip())  # Removes white spaces at the beginning of a string
# print(course.rstrip())  # Removes white spaces at the end of a string
# print(course.find("pro"))  # Find the index of a character in a string. If we don't have the intended character in a string, python will output a -1
# print(course.replace('p', 'j')) # Replaces all lower case p with j
# print("pro" in course) # Look to see if the character/sequence of character "pro" exists in the string and if it does, it will return a boolean value such as True/False
# print("swift" not in course) # Look to see if our string does not contain a character/sequence of character. In this case, we don't have "swift" and hence python will return True

''' Numbers '''

# x = 1 # this is an integer
# x = 1.1 # this is a float
# x = 1 + 2j  # complex number (a + bi)
# print(9/7)   # Float division
# print(9//7)  # Integer division
# print(9 % 7)  # Modulus that will find the remainder
# print(9 ** 7)  # exponential 

# x = 10
# x = x + 3
# x += 3 # Augmented assignment operation
# print(x)

''' Working with Numbers '''

# import math
# print (round(2.9))  # rounding up 
# print (abs(-2.9))  # absolute value of a number
# print(math.ceil(2.9))  # rounding up

''' Type conversation'''

# x = input("x: ")
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# int(x)
# float(x)
# bool(x)
'''Interesting Falsy boolean values'''
# ""
# 0
# None

# str(x)

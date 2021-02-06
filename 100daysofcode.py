# print("Hello World!\nHello world!!\nHello World!!!")

# # Concatination. we can add spaces after hello or before imtiaz or use empty space within a quotation and concatinate them.
# print("Hello " + " " + " Imtiaz")
# # Write your code below this line 👇
# print('Day 1 - Python Print Function')
# print('The function is declared like this:')
# print("print('what to print')")

# input () will get user input in console
# Then print() will print the word "Hello" and the user input
# print("Hello " + input("What is your name?"))

# print(len(input("What is your name? ")))

""" BMI Calculator  """


#🚨 Don't change the code below 👇
# height = input("enter your height in m: ")
# weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#height_as_float = float(height)
#weight_as_int = int(weight)
#bmi = weight_as_int/(height_as_float ** 2)


#bmi = int(weight)/(float(height)*float(height))
# bmi = int(weight) / float(height) ** 2
# bmi_as_int = int(bmi)
# print("Your BMI is: " , bmi_as_int)

""" How much time we have left in our life calculator """


"""My Code"""

# 🚨 Don't change the code below 👇
# age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# day = (90 - int(age)) * 365
# week = (90 - int(age)) * 52
# month = (90 - int(age)) * 12

# print(f"You have {day} days, {week} weeks, and {month} months left.")


""" Instructors code """

# 🚨 Don't change the code below 👇
# age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# years = 90 - int(age)
# months = round(years * 12)
# weeks = round(years * 52)
# days = round(years * 365)

# print(f"You have {days} days, {weeks} weeks, and {months} months left.")
# print ("Hello World")

""" Calculator Project """
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill?\n$"))
# tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
#If the bill was $150.00, split between 5 people, with 12% tip.
# people = int(input("How many people to split the bill between? "))
# bill_with_tip = tip / 100 * bill + bill
# tip_as_percentage = tip / 100
# total_tip_amount = tip_as_percentage * bill
# total_bill = total_tip_amount + bill
# print(total_bill)
#Each person should pay (150.00 / 5) * 1.12 = 33.6
# bill_per_person = total_bill/people
# final_amount = round(bill_per_person, 2)
# print(f"Each person should pay: ${final_amount}")
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

# 🚨 Don't change the code below 👇
# number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# if number % 2 == 0:
	# print("This is a even number")
# else:
	# print("You have entered an odd number")

''' Multiple if else statement '''

# print("Welcome to the show")
# height = int(input("Please enter height in cm "))
# if height >= 100:
#     print("You are approved to ride")
#     age = int(input("Please enter your age "))
#     if age > 5:
#         print("Your ticket cost $5")
#     elif age > 15:
#         print("Your ticket costs $15")
#     else:
#         print("Your ticket cost $25")
# else:
#     print("You are not eligible")

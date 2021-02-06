restricted_users = ['andrew','carol','daud']
user = input("Enter the name of a user\n")
if user not in restricted_users:
    print(user.title() + " , You have the access to the company database!!!")
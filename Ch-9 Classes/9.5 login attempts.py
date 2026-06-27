"""Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
Write another method called 
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0."""

class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        self.login_attempts = 0

    def increment_login_attempts(self):
        self.login_attempts += 1

    def describe_user(self):

        print(f"""-----------------------
First name : {self.first_name}
Last name : {self.last_name}
Login attempts : {self.login_attempts}""")

user_list = {
    "Suraj": User("Suraj", "Kumar"),
    "Aadesh": User("Aadesh", "Jogi"),
    "Parbhakar": User("Parbhakar", "Kumar"),
    "Aditya": User("Aditya", "Bhardwaj")
}



user_f_name = input("Enter Your First name : ").title()
user_l_name = input("Enter Your last name : ").title()


user = user_list.get(user_f_name)

if user:
    if user.last_name == user_l_name: 
        
        user.increment_login_attempts()
        
        print("\nLogin successful ✅")
        user.describe_user()
    else:
        print("\nLast name incorrect ❌")
else:
    print("\nUser not found ❌")
"""Make a class called User.
Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user’s information. 
Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both meth-ods for each user"""


class User:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def decribe_user(self):
        print(f"""-----------Profile summary------------
First name : {self.first_name}
Last name : {self.last_name}""")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name} To world of python")   
        
user_list ={
   "Suraj" : "Kumar",
   "Aadesh" : "Jogi",
   "Parbhakar" : "Kumar",
   "Aditya" : "Bhardwaj"
}

for f_name,l_name in user_list.items():
    user = User(f_name,l_name)

    user.decribe_user()
    user.greet_user()

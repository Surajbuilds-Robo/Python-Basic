"""Store the User class in one module, and 
store the Privileges and Admin classes in a separate module. 
In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly"""
from admin import *

admin = Admin("Aadesh", "Jogi")

admin.describe_user()
admin.greet_user()
admin.show_privileges()
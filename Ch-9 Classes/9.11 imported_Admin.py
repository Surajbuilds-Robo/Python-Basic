"""Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.
9-12. Multiple Modules: Store the User class in one module, and store the 
Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.
The Python Standard Library
The Python standard library is a set of modules included with every Python installation. Now that you have a basic understanding of how functions and classes work, you can start to use modules like these that other programmers have written. You can use any function or class in the standard library by including a simple import statement at the top of your file. Let’s look at one module, random, which can be useful in modeling many real-world situations.
"""

from admin import *

admin = Admin("Suraj", "Kumar")

admin.describe_user()
admin.greet_user()
admin.show_privileges()
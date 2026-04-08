
class User:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f"""-----------Profile summary------------
First name : {self.first_name}
Last name : {self.last_name}""")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name} to world of Python")


class Admin(User):

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Admin Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create Admin instance and call method
admin = Admin("Suraj", "Kumar")

admin.describe_user()
admin.greet_user()
admin.show_privileges()
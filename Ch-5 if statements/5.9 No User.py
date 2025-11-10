"""Add an if test to hello_admin.py to make sure the list of users is not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct mes-sage is printed"""

new_users = ['admin', 'Frank', 'GEORGE', 'alice', 'Hannah']

for user in new_users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else :
        print(f"Hello {user}, thank you for logging in again.")

del new_users

print(f"Create new Data of users then add new users")
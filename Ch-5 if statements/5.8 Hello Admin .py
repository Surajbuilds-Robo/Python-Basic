"""Make a list of five or more usernames, including the name 
'admin'. Imagine you are writing code that will print a greeting to each user after they log in to a website.
Loop through the list, and print a greeting to each user.
• If the username is 'admin', print a special greeting, such as Hello admin, would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Jaden, thank you for logging in again."""

saved_users = ['admin', 'Frank', 'GEORGE', 'alice', 'Hannah']

for user in saved_users:
    if user == 'admin':
        print("Hello admin, would you like to see a status report?")
    else :
        print(f"Hello {user}, thank you for logging in again.")


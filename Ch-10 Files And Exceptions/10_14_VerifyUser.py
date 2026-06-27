"""The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. 
We should modify it in case the current user is not the person who last used the program.
Before printing a welcome back message in greet_user(), ask the user if this is the correct username.
If it’s not, call get_new_username() to get the correct username.
"""

from pathlib import Path
import json

# Path to the JSON file
file_path = Path(__file__).parent / "username.json"


def get_new_username():
    """Prompt for a new username and store it."""
    username = input("What is your name? ")
    file_path.write_text(json.dumps(username))
    return username


def greet_user():
    """Greet the user and verify the stored username."""
    try:
        username = json.loads(file_path.read_text())
    except FileNotFoundError:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
    else:
        answer = input(f"Is '{username}' your username? (yes/no): ").lower()

        if answer == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")


greet_user()

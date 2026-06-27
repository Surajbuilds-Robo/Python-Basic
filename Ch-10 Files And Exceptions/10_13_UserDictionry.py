"""The remember_me.py example only stores one piece of information, the username. 
Expand this example by asking for two more pieces of information about the user, 
then store all the information you collect in a dictionary.
Write this dictionary to a file using json.dumps(), and read it back in using json.loads(). 
Print a summary showing exactly what your program remembers about the user."""

from pathlib import Path
import json

# File path
file_path = Path(__file__).parent / "user_info.json"

# Collect user information
user_info = {
    "username": input("Enter your username: "),
    "age": input("Enter your age: "),
    "favorite_color": input("Enter your favorite color: ")
}

# Store the dictionary in a JSON file
file_path.write_text(json.dumps(user_info, indent=4))

# Read the dictionary back from the file
saved_info = json.loads(file_path.read_text())

# Display the stored information
print("\nI remember the following information about you:")
print(f"Username       : {saved_info['username']}")
print(f"Age            : {saved_info['age']}")
print(f"Favorite Color : {saved_info['favorite_color']}")
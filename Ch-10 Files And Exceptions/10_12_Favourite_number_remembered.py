"""Combine the two programs you wrote in Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works."""

from pathlib import Path
import json

# Path to the JSON file
file_path = Path(__file__).parent / "favorite_number.json"

try:
    # Read the favorite number if it exists
    favorite_number = json.loads(file_path.read_text())

    print(f"I know your favorite number! It's {favorite_number}.")

except FileNotFoundError:
    # Ask the user for their favorite number
    favorite_number = input("What is your favorite number? ")

    # Store it in the JSON file
    file_path.write_text(json.dumps(favorite_number))

    print("I'll remember your favorite number!")
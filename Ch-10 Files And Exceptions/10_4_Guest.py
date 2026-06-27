"""Write a program that prompts the user for their name. When they respond, write their name to a file called guest.tx"""
from pathlib import Path

# File in the same directory as this script
file_path = Path(__file__).parent / "file.txt"

# Delete the file if it exists
if file_path.exists():
    file_path.unlink()
    print(f"{file_path.name} existed and has been deleted.")

# Get the person's name
name = input("Enter the person's name: ")

# Create the file and write the name
with file_path.open("w", encoding="utf-8") as file:
    file.write(f"Person Name: {name}\n")

print(f"{file_path.name} has been created successfully.")
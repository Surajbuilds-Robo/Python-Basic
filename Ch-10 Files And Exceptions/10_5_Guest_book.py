"""Write a while loop that prompts users for their name. Collect all the names that are entered, and then write these names to a file called 
guest_book.txt. Make sure each entry appears on a new line in the file"""

from pathlib import Path

# Create the file in the same directory as this script
file_path = Path(__file__).parent / "guest_book.txt"

print("Enter names (type 'quit' to stop):")

with file_path.open("w", encoding="utf-8") as file:
    while True:
        name = input("Enter your name: ")

        if name.lower() == "quit":
            break

        file.write(name + "\n")

print(f"\nAll names have been saved to '{file_path.name}'.")
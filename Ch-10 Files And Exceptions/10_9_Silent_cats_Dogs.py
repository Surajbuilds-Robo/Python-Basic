"""Modify your except block in Exercise 10-7 to fail silently if either file is missing."""


from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    file_path = Path(__file__).parent / filename

    try:
        with file_path.open("r", encoding="utf-8") as file:
            print(f"\nContents of {filename}:")
            print(file.read())

    except FileNotFoundError:
        pass
"""Make two files, cats.txt and dogs.txt. 
Store at least three names of cats in the first file and three names of dogs in the second file. 
Write a program that tries to read these files and print the contents of the file to the screen. 
Wrap your code in a try-except block to catch the FileNotFound error, and
 print a friendly message if a file is missing. 
Move one of the files to a dif-ferent location on your system, and 
make sure the code in the except block executes properly"""


from pathlib import Path

files = ["cats.txt", "dogs.txt"]

for filename in files:
    file_path = Path(__file__).parent / filename

    try:
        with file_path.open("r", encoding="utf-8") as file:
            print(f"\nContents of {filename}:")
            print(file.read())

    except FileNotFoundError:
        print(f"\nSorry, '{filename}' could not be found.")
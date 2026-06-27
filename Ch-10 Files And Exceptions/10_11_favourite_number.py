"""Write a program that prompts for the user’s favorite number. Use json.dumps() to store this number in a file. Write a separate pro-gram that reads in this value and 
prints the message “I know your favorite  number! It’s _____.”"""


from pathlib import  Path

import json


num = int(input("Enter Your favourite number : "))

path = Path('fav_number.json')
content = json.dumps(num)
path.write_text(content)

contents = path.read_text()

print(f"Your Favourite number is : {contents}")

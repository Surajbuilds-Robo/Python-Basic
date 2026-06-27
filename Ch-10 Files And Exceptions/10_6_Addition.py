"""One common problem when prompting for numerical input occurs when people provide text instead of numbers. 
When you try to convert the input to an int, you’ll get a ValueError. 
Write a program that prompts for two numbers. 
Add them together and print the result. 
Catch the ValueError if either input value is not a number, and print a friendly error message. 
Test your program by entering two numbers and then by entering some text instead of a numbe
"""

try:
    num1 = int(input("Enter the first number: "))
except ValueError:
    print("❌ The first value is not a valid number.")
    exit()

try:
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("❌ The second value is not a valid number.")
    exit()

print(f"The sum is: {num1 + num2}")
"""Wrap your code from Exercise 10-5 in a 
while loop so the user can continue entering numbers, 
even if they make a mistake and enter text instead of a number."""


while True:
    try:
        num1 = int(input("Enter the first number (or 'q' to quit): "))
        num2 = int(input("Enter the second number: "))

        print(f"The sum is: {num1 + num2}")

    except ValueError:
        print("❌ Invalid input! Please enter numbers only.")

    choice = input("\nDo you want to continue? (y/n): ").lower()

    if choice == "n":
        print("Goodbye!")
        break
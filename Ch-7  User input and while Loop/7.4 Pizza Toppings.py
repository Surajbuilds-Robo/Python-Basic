"""Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza"""

topping = input("Enter topping u like to add: ")

while topping != "quit":
    topping = input("Enter a pizza topping (or 'quit' to stop): ")
    if topping != "quit":
        print(f"I'll add {topping} to your pizza.")

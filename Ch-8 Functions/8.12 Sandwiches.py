"""Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sand-wich that’s being ordered. Call the function three times, using a different num-ber of arguments each time."""

def make_sandwich(*items):
    print("Sandwich order:")
    for item in items:
        print(item)

make_sandwich("ham", "cheese")
make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("chicken", "bacon", "cheese", "onions")

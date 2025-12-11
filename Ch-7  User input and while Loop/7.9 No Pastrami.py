"""Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code  near the beginning of your program to print a message saying the deli has  run out of pastrami, and then use a while loop to remove all occurrences of 
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up  in finished_sandwiches"""

sandwich_orders = [
    "veg Sandwich", "Non-veg Sandwich", "Tuna Sandwich",
    "Veg Sandwich", "Grilled Sandwich", "Club Sandwich",
    "Cheese Sandwich", "Ham Sandwich", "Egg Sandwich"
]

sandwich_orders.append("pastrami")
sandwich_orders.append("pastrami")
sandwich_orders.append("pastrami")

print("The deli has run out of pastrami!")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

finished_sandwiches = []

print("\nMaking your sandwiches...\n")

for order in sandwich_orders:
    print(f"I made your {order}.")
    finished_sandwiches.append(order)

print("\nFinished sandwiches:")
for s in finished_sandwiches:
    print(s)

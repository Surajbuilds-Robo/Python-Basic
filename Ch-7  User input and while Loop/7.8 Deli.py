"""Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. 
Loop through the list of sandwich orders and 
print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made."""

sandwich_orders = ["veg Sandwich", "Non-veg Sandwich ","Tuna Sanwich","Veg Sandwich","Grilled Sandwich","Club Sandwich","Cheese Sandwich","Ham Sandwich","Egg Sandwich"]

for i in sandwich_orders:
    print(i)

name = input("enter what you would like to have : ").title()
if name in sandwich_orders:
    print(f"We Have made your {name}\n")
    sandwich_orders.remove(name)
    print("listed below can be made : \n")
    for sandwich in sandwich_orders:
        print(sandwich)
else:
    print("\n")



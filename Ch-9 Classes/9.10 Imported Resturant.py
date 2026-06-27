"""using your latest Restaurant class,store it in a mod-ule. 
Make a separate file that imports Restaurant. 
Make a Restaurant instance, and call one of Restaurant’s methods 
to show that the import statement is work-ing properly."""

from resturant import *

restaurant = Restaurant("Spice Hub", "Indian")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
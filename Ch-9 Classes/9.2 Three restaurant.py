"""Three Restaurants: Start with your class from Exercise 9-1. 
Create three different instances from the class, and call describe_restaurant() for each instance"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"""Cuisine Type: {self.cuisine_type}
               """)

    def open_restaurant(self):

        print(f"{self.restaurant_name} is now open!")



restaurant1 = Restaurant("Spice Hub", "Indian")
restaurant2 = Restaurant("Toko Hub", "Chiniese")


restaurant1.describe_restaurant()
restaurant2.describe_restaurant()

restaurant1.open_restaurant()
restaurant2.open_restaurant()

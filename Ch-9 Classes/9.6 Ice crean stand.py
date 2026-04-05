"""An ice cream stand is a specific kind of restaurant. 
Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162)
 or Exercise 9-4 (page 166). 
Either version of the class will work; 
just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
write a method that displays these flavors. 
Create an instance of IceCreamStand, and call this method."""

class Restaurant:

    number_served = 0
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        # Print open status
        print(f"{self.restaurant_name} is now open!")
    
    def costumer_served(self,number):
        self.number_served +=number
        return self.number_served

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0   # ✅ instance attribute

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def customer_served(self, number):
        self.number_served += number
        return self.number_served


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)  # ✅ call parent first
        self.flavors = flavors

    def display_flavors(self):   # ✅ required method
        print("Available Ice Cream Flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Data
flavor_list = ["Vanilla", "Chocolate", "Strawberry", "Butterscotch"]

# Object
restaurant = IceCreamStand("Spice Hub", "Indian", flavor_list)

# Calls
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.display_flavors()
print(f"No of customers served: {restaurant.costumer_served(45)}")

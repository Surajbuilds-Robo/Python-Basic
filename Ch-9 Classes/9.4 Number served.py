"""Start with your program from Exercise 9-1 (page 162). 
Add an attribute called number_served with a default value of 0. 
Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, 
and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. 
Call this method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. 
Call this method with any number you like that could represent how many customers were served in, say, a day of business
"""

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



restaurant = Restaurant("Spice Hub", "Indian")


print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
print(f"No of customer served : {restaurant.costumer_served(45)}")


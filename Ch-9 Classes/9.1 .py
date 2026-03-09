"""Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indi-cating that the restaurant is open.
Make an instance called restaurant from your class. 
Print the two attri-butes individually, and then call both methods."""

class Resturant:

    def __init__(self,resturant_name , cuisine_type):
        resturant_name = self.describe_resturant()
        cuisine_type = self.describe_resturant()
    def describe_resturant (self,eresturant_name,cuisine_type):
        print(f"From {self.resturant_name} , i like, this {cuisine_type} type") 


a = Resturant.
"""Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity to 65 if it isn’t already. 
Make an electric car with a default battery size, call get_range() once, 
and then call get_range() a second time after upgrading the battery. 
You should see an increase in the car’s range"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return f"{self.year} {self.make} {self.model}".title()

    def read_odometer(self):
        """Print the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Increase odometer reading."""
        self.odometer_reading += miles


class Battery:
    """Model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize battery size."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Describe the battery."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print the range based on battery size."""
        if self.battery_size == 40:
            range_val = 150
        elif self.battery_size == 65:
            range_val = 225
        else:
            range_val = 0

        print(f"This car can go about {range_val} miles on a full charge.")

    def upgrade_battery(self):
        """Upgrade battery to 65 if not already."""
        if self.battery_size != 65:
            self.battery_size = 65


class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize parent attributes + battery."""
        super().__init__(make, model, year)
        self.battery = Battery()


# 🔍 Test the program
my_leaf = ElectricCar('nissan', 'leaf', 2024)

print(my_leaf.get_descriptive_name())

# Before upgrade
my_leaf.battery.get_range()

# Upgrade battery
my_leaf.battery.upgrade_battery()

# After upgrade
my_leaf.battery.get_range()


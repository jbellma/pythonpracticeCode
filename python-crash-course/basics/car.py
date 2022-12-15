class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retun a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', '2004')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# Modifying an attribute's value directly

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Modifying an attribute’s value through a method.

my_new_car.update_odometer(45)
my_new_car.read_odometer()

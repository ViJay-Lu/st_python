from car import Car
from car import ElectricCar

"""
2024 Bmw X6
This car has 23 miles on it.
"""
my_new_car = Car("bmw","X6",2024)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
print("\n")

"""
2024 Tesla Model S
This car has 30 miles on it.
this car has a 70-kWh battery.
This car can go approximately 240 miles on a full charge.
"""
my_tesla =  ElectricCar("tesla","model S",2024)
print(my_tesla.get_descriptive_name())
my_tesla.odometer_reading = 30
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


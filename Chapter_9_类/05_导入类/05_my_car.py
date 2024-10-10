from car import Car
from car import ElectricCar
"""
#一个模块导入多个类的写法,用","分隔
from car import Car,ElectricCar,Battery

#也可以导入整个模块
import car

#导入模块中所有类
from car import *
"""




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


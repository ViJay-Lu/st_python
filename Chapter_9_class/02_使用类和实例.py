class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #指定默认值
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles < 0:
            print("Sorry, you can't roll back an odometer!")
            return
        else:
            self.odometer_reading += miles

my_car = Car('Tesla', 'model Y', 2021)
print(my_car.get_descriptive_name())
"""修改类属性"""
#1：直接修改
my_car.odometer_reading = 100
my_car.read_odometer()
#2：通过方法修改
my_car.update_odometer(500)
my_car.read_odometer()
my_car.increment_odometer(100)
my_car.read_odometer()
my_car.increment_odometer(-100)
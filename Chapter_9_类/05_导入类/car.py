class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
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

    def fill_gas_tank(self):
        print("this is Car fill_gas_tank")


class Battery():
    def __init__(self,battbattery_size=70):
        self.battery_size=battbattery_size

    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range) + " miles on a full charge."
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        #super()是特殊函数，将子类与父类关联起来
        super().__init__(make, model, year)
        self.battery = Battery()
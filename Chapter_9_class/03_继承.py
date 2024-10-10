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

    def test01(self):
        print("this is test01")

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

    #重写父类方法
    def fill_gas_tank(self):
        print("this is ElectricCar fill_gas_tank")
    """
    当类中的函数清单很多时，可以将类的一部分独立定义一个类并提取出来，如下面这两个类成员函数
    def describe_battery(self):
        print("this car has a " + str(self.battery_size) + "-kWh battery.")
    def test01(self):
        print("this is test01")
    """

my_tesla = ElectricCar('Tesla', 'model Y', 2024)
#2024 Tesla Model Y
print(my_tesla.get_descriptive_name())

#this car has a 70-kWh battery.
#my_tesla.describe_battery() 抽取类中方法前的写法

#提取后的写法
my_tesla.battery.describe_battery()
my_tesla.battery.test01()

#this is ElectricCar fill_gas_tank
my_tesla.fill_gas_tank()

#This car can go approximately 240 miles on a full charge.
my_tesla.battery.get_range()
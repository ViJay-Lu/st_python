"""以下为python2.7中类与继承的写法"""
class Car1(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

class ElectricCar1(Car1):
    def __init__(self, make, model, year):
        super(ElectricCar1,self).__init__(make, model, year)
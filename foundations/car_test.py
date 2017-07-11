# 如果不继承的话 无需写()
class Car:
    def __init__(self, make, model, year=2015):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 200

    def update_odometer(self, mileage):
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('You can\' roll back odometer')

    def fill_gas_tank(self):
        print('gas tank')

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def descriptive_name(self):
        print('%s %s %s' % (self.make, self.model, self.year))

    def read_odometer(self):
        print('This is car %s miles on it' % self.odometer_reading)


class ElectricCar(Car):
    def __init__(self, make, model, year=2015):
        # 2.7 需要在括号中写出类名、self两个参数
        super().__init__(make, model, year)

    def fill_gas_tank(self):
        print('no gas tank')

bmw = Car('Subaru', 'yibao', 2016)
bmw.update_odometer(15)
bmw.descriptive_name()
bmw.read_odometer()

electric_car = ElectricCar('Tesla', 'Model-S', 2017)
electric_car.descriptive_name()

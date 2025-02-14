class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f'{self.make} {self.model} {self.year}'
    def __repr__(self):
        return f'{self.make} {self.model} {self.year}'

class ElectricCar(Car):
    def __init__(self, make, model, year,battery_capacity):
        super().__init__(make,model,year)
        self.battery_capacity = battery_capacity
    def __str__(self):
        super().__str__()
        print(f'battery capacity: {self.battery_capacity}kWh')


class Person:
    def __init__(self, name, age, ):
        print(f'Hi, my name is {name} and I am {age} years old')




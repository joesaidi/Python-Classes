class Car:
    def __init__(self,size,horse_power,make,model):
        self.make = make
        self.model = model
        self.engine = Engine(horse_power)
        self.wheel = [Wheel(size) for i in range(4)]
    
    def display_car(self):
        return f'{self.make} {self.model} with horse power of {self.engine.horse_power} and wheel size of {self.wheel[1].size} inches'

class Wheel:
    def __init__(self,size):
        self.size = size

class Engine:
    def __init__(self,horse_power):
        self.horse_power = horse_power


car = Car(make='Benz',model='C200',horse_power=400,size=18)
print(car.display_car())
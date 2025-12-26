from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def go(self):
        pass


class Car(Vehicle):
    def stop(self):
        return "Car is stopping"

    def go(self):
        return "Car is moving"


class Bike(Vehicle):
    def stop(self):
        return "Bike is stopping"

    def go(self):
        return "Bike is moving"


class Bus(Vehicle):
    def stop(self):
        return "Bus is stopping"

    def go(self):
        return "Bus is moving"


car = Car()
bike = Bike()
bus = Bus()
print(car.stop()) 
print(bike.stop())
print(bus.go())

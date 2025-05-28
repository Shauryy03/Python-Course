# inheritance

class Car:
    colour = "black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stoped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name


Car1 = ToyotaCar("fortuner")
Car2 = ToyotaCar("prius")

print(Car1.start())
    
# abstraction

class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk= False

    def start(self):
        self.clutch=True
        self.acc=True
        print("car statred")
        
car1 = Car()
car1.start()

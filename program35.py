
# static method

class Student:
    def __init__(self, name, m1,m2,m3):
        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @staticmethod
    def college():
        print("LNCT Bhopal")

    def printavg(self):
        print((self.m1+self.m2+self.m3) / 3)

s1 = Student("karan",89,96,88)
s1.printavg()
s1.college()

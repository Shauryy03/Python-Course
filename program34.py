# ques-create student class that take name and marks of 3 subject as argument in constructor then create the method to print avg

class Student:
    def __init__(self, name, m1,m2,m3):
        self.name = name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def printavg(self):
        print((self.m1+self.m2+self.m3) / 3)

s1 = Student("karan",89,96,88)
s1.printavg()

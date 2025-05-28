# contructor 

class Student:
        
        # default constructor
    def __init__ (self):
        pass

        # parameterized constructor
    def __init__(self,name,marks):
        # print(self)
        self.name = name
        self.marks = marks
        print("adding new student")


# internally self ka mtlv whi h jo hum s1 object ki baat kr rhe
s1=Student("shaury patel", 98)
print(s1.name, s1.marks)
# print(s1)


s2=Student("karan", 90)
print(s2.name, s2.marks)

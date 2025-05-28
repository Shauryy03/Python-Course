# del keyword

class Student :
    def __init__(self, name):
        self.name=name

s1 = Student("shaury")
print(s1.name)
del s1.name
print(s1.name)  # Student' object has no attribute 'name' ye aarha h q ki name attribue to delete kr diye h
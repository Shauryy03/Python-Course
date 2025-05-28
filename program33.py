# methods

class Student :
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def hellow(self):
        print("hellow",self.name)
    def score(self):
        return self.marks
    

s1 = Student("saurabh",98)
s1.hellow()
print(s1.score())
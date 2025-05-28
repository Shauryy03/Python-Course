# @classmethod

class Person:
    name = "anonymous"
    @classmethod
    def changeName (cls, name):
        cls.name = name

    # def changeName (self, name):
    #     self.name = name #does not change the the name attribute of class, this create new name attribute


P1 = Person()
P1.changeName("shaury")
print(P1.name)
print(Person.name)
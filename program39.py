# private attribute and mmethod

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass  #to made function and method private we have to add two underscore before the name of attribute and function 
 
acc1 = Account("10001", "Abcd")
print(acc1.acc_no)
print(acc1.__acc_pass) #it will give us error

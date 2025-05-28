# create account class with two attribute - balance, account-number 
# create method for debit, credit and printing balance

class Account:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance

    def credit(self, cre_amount):
        self.balance +=cre_amount
        print("Rs.",cre_amount,"was credited")
        print("total balance =",self.print_bal())

    def debit(self, deb_amount):
        self.balance -=deb_amount
        print("Rs.",deb_amount,"was debited")
        print("total balance =",self.print_bal())

    def print_bal(self):
        return self.balance

A1 = Account(10001,500)
A1.debit(100)
A1.debit(380)
A1.credit(90000)
        
        
        
        
        
        

#create student class that takes name & marks of 3 subjects as arguments in constructor.
#then create a method to print the average.
class student:
    def __init__(self,name,math_marks,ch_marks,py_marks):
        self.name = name
        self.math_marks = math_marks
        self.ch_marks = ch_marks
        self.py_marks = py_marks
    
    def average(self):
        print((self.math_marks + self.ch_marks + self.py_marks)/3)

s1 = student("rajesh",65,76,40)
s1.average()
s1.name = "tony" # changing the name
print(s1.name)

#create account class with 2 attributes balance & account no.
#create methods for debit, credit & printing the balance.

class account:
    def __init__(self,ac_no,balance):
        self.ac_no = ac_no
        self.balance = balance

    def credit(self,amount):
        self.balance = self.balance + amount
        print("you credited",amount,"from your account","your balance is",self.balance)

    def debit(self,amount):
        self.balance = self.balance - amount
        print("you debited",amount,"from your account","your balance is",self.balance)

a1 = account(123,10000)
a1.credit(5000)
print(a1.balance)
a1.debit(5000)
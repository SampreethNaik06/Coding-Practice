# Class Variables

# class variables can be shared amoung all instances of a class while instance variables are accessible among only that instances

class Employee:

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return '{},{}'.format(self.first,self.last)


    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amt)

employee_1 = Employee('ampreeth','naik',90000)
employee_2 = Employee('lan','merill',90000)


# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)


print(Employee.__dict__)

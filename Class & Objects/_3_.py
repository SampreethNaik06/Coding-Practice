 # regular methods class methods and static methods

# regular methods automatically takes the instance as the first argument i.e self 



class Employee:

    num_of_employee = 0 

    raise_amt = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_employee += 1 # this works when we create a employee

    def fullname(self):
        return '{},{}'.format(self.first,self.last)


    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amt = amount


employee_1 = Employee('ampreeth','naik',90000)
employee_2 = Employee('lan','merill',90000)


# print(employee_1.pay)
# employee_1.apply_raise()
# print(employee_1.pay)


# print(Employee.__dict__)



print(Employee.num_of_employee)
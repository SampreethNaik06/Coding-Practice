# OOPs in pythons 

# allow us to logically group datas and functions :

class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last 
        self.phone = pay
        self.email = first + "." + last + "@company.com"\

    def fullname(self):
        return '{},{}'.format(self.first,self.last)

employee_1 = Employee('ampreeth','naik',90000)
employee_2 = Employee('lan','merill',90000)



print(employee_1.fullname())
print(employee_1.email)


print(Employee.fullname(employee_1))
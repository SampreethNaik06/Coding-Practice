# to check if the person is eligible for income tax or not

def check_icome_tax(income,age):
    if age>18:
        if income>50000: 
            print("the person is eligible for income tax")
        else:
            print("the person is not eligible for income tax")
    else:
        print("the person is not eligible for income tax as age is less than 18")
        
check_icome_tax(60000,25)
check_icome_tax(40000,30)

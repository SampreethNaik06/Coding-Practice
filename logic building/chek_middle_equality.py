# to check if in the three digit number the sum of first and last digit is equal to the middle one

def check_equality(num):
    num  = str(num)
    if int(num[0])+int(num[2]) == int(num[1]):
        print("it is equal")
    else:
        print("it is not equal")
        
check_equality(143) 
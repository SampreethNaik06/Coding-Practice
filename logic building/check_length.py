# to check the length of the number and return the result 
def check_length(num):
    number = str(num)
    if len(number) == 2:
        print("the number is 2 digit")
    elif len(number) == 3:
        print("the number is 3 digit")
    elif len(number) == 4:
        print("the number is 4 digit")
    else:
        print("invalid input")
        
check_length(12)
check_length(123)
check_length(1234)
check_length(12345)
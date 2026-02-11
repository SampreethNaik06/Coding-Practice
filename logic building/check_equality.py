# check if the first and last digits are equalin a 4 digit number
def check_equality(num):
    number = str(num)
    if len(number) != 4:
        print("invalid input")
    elif number[0] == number[3]:
        print("first and last digits are equal")
    else:   
        print("first and last digits are not equal")
        
        
check_equality(1234)
check_equality(1221)
    
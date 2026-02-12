# to check if the numbr is multiple of 7 or ends with 7 

def check_7(n):
    if n% 7 ==0 and n%10 == 7:
        print("number is multiple of 7 and ends with 7")
    elif n% 7 ==0:
        print("number is multiple of 7")
    else:
        print("number is not multiple of 7")
        
        
check_7(14)
check_7(27) 
check_7(28)
check_7(37)
check_7(70)
check_7(77)
# to check if one number is multiple of another 
def check_multiple(a,b):
    if (a%b ==0 and b!=0 )or (b%a ==0 and a!=0):
        print("a and b are multiples of each other ")
    else:
        print("none is multiple of other")  
        
        
        
        
check_multiple(4,2)
check_multiple(2,4)
check_multiple(3,5)

        
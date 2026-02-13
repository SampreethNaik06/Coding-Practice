#to check if the givn two numbers are positive and their sum is greater than 100
def check_sum(a,b):
    if a>0 and b>0 :
        if a+b> 100:
             print("both the numbers are positive and their sum is greater than 100")
        else:
            print("both the numbers are positive but their sum is not greater than 100")
    else:
        print("one or both numbers are not positive")
        
             
check_sum(60,50)
check_sum(30,40)
check_sum(-10,50)
check_sum(20,-5)
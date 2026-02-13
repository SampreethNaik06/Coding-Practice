# check median of three nubners
def check_median(a,b,c):
    total  = a + b + c
    maximun = max(a,b,c)
    minimum = min(a,b,c)
    median = total - maximun - minimum
    print(median)
    
    
check_median(10,20,30)
check_median(5,15,10)
check_median(25,5,15)
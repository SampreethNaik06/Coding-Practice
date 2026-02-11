# to check the number of days in the particular month

def days_in_month(month):
    if month in [1,3,5,7,8,10,12]:
        print("31 days")
    elif month in [4,6,9,11]:
        print("30 days")  
    else:
        print("invalid input")
        
days_in_month(2)
days_in_month(1)    
days_in_month(4)
days_in_month(13)
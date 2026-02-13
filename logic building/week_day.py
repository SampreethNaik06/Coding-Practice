# to take numbers for (1-7 ) and print if its weekday or weekend
def week_day(num):
    if num in [1,2,3,4,5]:
        print("weekday")
    elif num in [6,7]:
        print("weekend")
    else:
        print("Invalid input")
        
week_day(3)
week_day(6)
week_day(8)

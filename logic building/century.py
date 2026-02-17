## to take a year and check the century 
def find_century(year):
    century = (year - 1) // 100 + 1
    
    if 10 <= century % 100 <= 20:
        suffix = "th"
    elif century % 10 == 1:
        suffix = "st"
    elif century % 10 == 2:
        suffix = "nd"
    elif century % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"
    
    print(f"{century}{suffix} century")

find_century(1905)

    
    
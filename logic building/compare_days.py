# to compare two days and check which day comes first 

def compare_dates(d1, m1, d2, m2):
    if m1 < m2:
        print("First date comes first")
    elif m1 > m2:
        print("Second date comes first")
    else:  # same month
        if d1 < d2:
            print("First date comes first")
        elif d1 > d2:
            print("Second date comes first")
        else:
            print("Both dates are the same")

# Example
compare_dates(15, 3, 10, 4)

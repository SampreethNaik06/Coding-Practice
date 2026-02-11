# to check where the given coordinates are in which quadrant
def check_coordinates(x, y):
    if x == 0 or y == 0:
        if x == 0 and y == 0:
            print("Origin")
        elif x == 0:
            print("Y-axis")
        else:
            print("X-axis")
    else:
        if x > 0:
            if y > 0:
                print("1st quadrant")
            else:
                print("4th quadrant")
        else:
            if y > 0:
                print("2nd quadrant")
            else:
                print("3rd quadrant")

check_coordinates(1,2)
check_coordinates(-1,2)
check_coordinates(-1,-2)
check_coordinates(1,-2)
check_coordinates(0,0)

# to find the third angle of a triangle when two angles are given

def check_angle(a,b):
    if a <0 or b<0 :
        print("angles cannot be negative")
    elif a+b >= 180:
        print("the sum of angles cannot be greater than or equal to 180")
    else:
        c = 180 - (a+b)
        print(f"the third angle of the triangle is {c}")
        
check_angle(60, 90)
check_angle(120, 30)
check_angle(100, 90)

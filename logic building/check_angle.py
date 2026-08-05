# to find the third angle of a triangle when two angles are given

def checkangle(x,y):
    if x<0 & y<0:
        print("angles cannot be in negetive")
    elif x+y > 180 :
        print("sum 0f angles in a triangle annot be greater thn 180 degree")
    return 

    t_angle = 0
    t_angle = 180 -(x+y)
    print(f"{t_angle} is the third angle") 

        
checkangle(60, 90)
checkangle(120, 30)
checkangle(100, 90)

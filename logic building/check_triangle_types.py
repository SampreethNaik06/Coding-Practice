#to check the type of triangle
def check_triangle(a,b,c):
    if a<=0 or b<=0 or c<=0:
        print("not a triangle")
    elif a == b == c:
        print("equilateral triangle")
    elif a==b or b==c or c==a:
        print("isoceles triangle")
    else:
        print("scalene triangle")
        
        
check_triangle(3,4,5)
check_triangle(2,2,3)   
check_triangle(3,3,3)
check_triangle(-1,2,3)
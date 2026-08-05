# to check if trianggle
def check_triangle(a, b, c):
    if a<=0 or b<=0 or c<=0:
        print("negetive value erro")
    elif not(a+b>c and b+c>a and a+c>b):
        print(" triangle")
    else:
        print(" not a triangle")
        
check_triangle(1, 3, 3)
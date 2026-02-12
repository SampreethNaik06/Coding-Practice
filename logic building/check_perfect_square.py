# to check if the given number is a perfect square or not without math function

def perfect_square(num):
    if num < 0:
        print("negative numbers cannot be perfect squares")
        return
    i = 0
    while i*i<num:
        i+=1
    if i*i == num:
        print("the number is a perfect square") 
    else:
        print("the number is not a perfect square")
        
perfect_square(16)
perfect_square(20)
perfect_square(-4)



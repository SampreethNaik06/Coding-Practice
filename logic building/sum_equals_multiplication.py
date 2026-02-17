# to check if the sum of digits is equal to multiplication of digits
def checkcase(n):
    sum_digits = 0
    mul = 1
    n = str(n)
    
    for i in n:
        sum_digits += int(i)
        mul *= int(i)
        
    if sum_digits > mul:
        print("sum is greater than mul")
    else:
        print("sum is not greater than mul")

checkcase(123)

# to check if the sum of digits is equal to multiplication of digits

def checkcase(n):
    sum = 0
    mul = 1
    n = str(n)
    
    for i in (n):
        sum+= int(i)
        mul += int(i)

    if sum == mul:
            print("sum == mul")
    else:
            print("is not equal")


checkcase(123)
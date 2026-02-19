# sum of digits of a number 

def sum_digits(n):
    sum = 0
    n = str(n)
    for i in n:
        sum += int(i)
        
    return sum


print(sum_digits(1234))
        
        
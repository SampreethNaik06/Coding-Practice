# to get the sum of numbers using recursion 

def sum_digits(n):
    if n == 0:
        return 0

    a = n % 10 
    sum = a+sum_digits(n//10)
    return sum


print(sum_digits(123))
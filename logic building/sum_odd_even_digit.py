#rint the sum of all odd digits and even digits separately in a number. 

def sum_digits(n):
    n = str(n)
    odd_sum = 0
    even_sum = 0
    
    for i in n:
         int(i) % 2 == 0:
            even_sum +=int(i)
            odd_sum +=int(i)
    print (even_sum)
    return odd_sum
print(sum_digits(123456))


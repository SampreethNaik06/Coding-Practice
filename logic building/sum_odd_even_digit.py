# Print the sum of all odd digits and even digits separately in a number. 

def sum_digits(n):
    n_str = str(n)
    odd_sum = 0
    even_sum = 0
    
    for i in n_str:
        val = int(i)
        if val % 2 == 0:
            even_sum += val
        else:
            odd_sum += val
            
    print("Even sum:", even_sum)
    print("Odd sum:", odd_sum)

sum_digits(123456)


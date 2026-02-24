# Print all numbers whose sum of digits is odd  (1–100). 

def sum_digits_odd():
    count = 0
    
    for i in range(1, 101):
        num = i
        digit_sum = 0
        
        while num > 0:
            digit = num % 10
            digit_sum += digit
            num = num // 10
            
        if digit_sum % 2 != 0:
            count += 1
            
    return count

print("Total numbers:", sum_digits_odd())
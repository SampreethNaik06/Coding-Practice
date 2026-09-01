def Armstrong_number(n):
    original = n
    num_digits = len(str(n))
    total_sum = 0
    
    while n > 0:
        digit = n % 10
        total_sum += digit ** num_digits
        n = n // 10

    return total_sum == original

print(Armstrong_number(371))  # Output: True
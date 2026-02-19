# to check if the number is prime or not
def check_prime(num):
    if num == 0 or num ==1:
        return False
    
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    
    return True
    
print(check_prime(97))
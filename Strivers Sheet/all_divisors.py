# all divisors
import math

def divisor(n):
    divisors = []
    # Loop from 1 to floor(sqrt(n))
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            # Avoid adding the square root twice if n is a perfect square
            if n // i != i:
                divisors.append(n // i)
    
    divisors.sort()  # Optional: keep them sorted
    print(divisors)

divisor(36)
# Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]

# Print factorial of each number from 1 to n. 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 100
for i in range(1, n + 1):
    print(f"{i}! =", factorial(i))
# to check for fibonacci sequence

def fibonacci(n):
    if n <= 1:
        return n
    
    a = 0
    b = 1
    
    for i in range(n):
        a, b = b, a + b
        
    return a
print(fibonacci(50))
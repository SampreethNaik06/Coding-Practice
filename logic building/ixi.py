# Print a pattern where each row i prints i*i. 

def pattern(n):
    for i in range(1, n + 1):
        print("*" * i)

pattern(5)

def new_pattern(n):
    for i in range(n,0,-1):
        print("*"*i)
new_pattern(10)
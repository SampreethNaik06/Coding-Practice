# to count numbers in a digits recursively

def count_numbers(n):
    if n == 0:
        return 1
    return 1 + count_numbers(n //10)
    
print(count_numbers(100))


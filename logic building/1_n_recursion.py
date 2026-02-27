# to print from 1 to n using recursion

def print_1_n(n):
    if n == 0:
        return
    print_1_n(n - 1)
    print(n)

print_1_n(10)

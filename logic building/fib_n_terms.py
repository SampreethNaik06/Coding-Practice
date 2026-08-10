# to find the fibonacci until the n terms

def fib(n):
    if n == 0:
        return 0
    if  n ==  1:
        return 1
    return fib(n-1) + fib(n-2)


def fib_n_terms(terms):

    if terms < 0:
        print("enter a positive integer")
    
    for i in range(terms):
        print(fib(i), end ="")
        print()
    return



fib_n_terms(10)


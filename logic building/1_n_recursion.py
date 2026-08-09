# to print from 1 to n using recursion
def _1_n_recursion(n):
    if  n <= 0 :
        return
    _1_n_recursion(n-1)
    print(n)

_1_n_recursion(10)
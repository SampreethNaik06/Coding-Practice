# to print in reverse from n-1 using recursion

def one_n_reverse(n):
    if n == 0:
        return
    print(n)
    one_n_reverse(n - 1)

one_n_reverse(5)
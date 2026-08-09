# sum from 1 to n using recursion 

def sum_1_n(n):
    if n<=0:
        return n
    return n+(sum_1_n(n-1))

sum_1_n(100)
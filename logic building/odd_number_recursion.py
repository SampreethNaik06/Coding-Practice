# to print odd numbers using recursion

def odd_number(n):

    if n < 0:
        return 0

    odd_number(n-1)

    if n% 2 != 0:
        print(n)


odd_number(15) 
    

# to find all the even numbers in a range of a given number

def even_number(n):
    if n < 0 : 
        return 
    even_number(n-1)

    if n % 2 == 0:
        print(n)

    return

even_number(30)
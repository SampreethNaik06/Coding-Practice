# to print product of digits in a given number


def product_digits(n):
    product = 1
    n = str(n)
    for i in (n):
        product *= int(i)
    print(product)
    
product_digits(1234)
        
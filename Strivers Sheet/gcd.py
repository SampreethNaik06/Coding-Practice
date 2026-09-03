# gcd of 2 numbers

def gcd(a,b):

    while (a>0 and  b>0):
        if a>b:
            a= a%b
        else:
            b = b % a
    if a == 0:
        print(f"gcd ={b} ")
    else:
        print(f"gcd = {a}")

    return 


gcd(52,10)

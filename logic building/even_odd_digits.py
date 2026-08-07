# counting even and odd digits in a number 

def even_odd(n):
    evn_cnt = 0
    odd_cnt = 0

    if n < 0:
        print("enter a bigger number")

    while n > 0:
        dgt = n % 10 
        if dgt % 2 == 0:


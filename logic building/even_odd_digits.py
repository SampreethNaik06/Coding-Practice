# counting even and odd digits in a number 

def even_odd(n):
    evn_cnt = 0
    odd_cnt = 0

    if n < 0:
        print("enter a bigger number")

    while n > 0:
        dgt = n % 10 
        if dgt % 2 == 0:
            evn_cnt += 1
        else:
            odd_cnt += 1

        n = n // 10
    print(f"{evn_cnt} is the even count and {odd_cnt} is the odd count")


even_odd(112435601230)



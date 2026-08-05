# dividing a number until its small

def number(num):

    if num < 5:
        print("add a bigger number")
    

    while num>=5:
        num = num // 2

    print("the number is reduced to less than 5 ")



number(100)

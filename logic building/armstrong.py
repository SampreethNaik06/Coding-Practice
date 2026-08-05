#  to check if the number is a armstrong number 

def armstrong_number(num):
    num_str = str(num)
    total = 0
    l = len(num_str)

    for i in num_str:
        total += int(i)**l

    if total == num:
        print("Armstrong number")
    else:
        print("Not an Armstrong number")


# to cheeck the sum of even numbers in a range

def sum_even(num):

    sum = 0
    current = 1

    while current<=num:
        if current % 2 ==0:
            current+= sum

        current+= 2

    print(sum)


sum_even(10)

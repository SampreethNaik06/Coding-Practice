# to print sum of all odd natural numbers

def odd_sum(n):
    sum = 0

    for  i in range(1,n+1,2):
        sum+= i

    print(sum)

odd_sum(100)


# for i in range(1,n+1,2) this can also be used instrad of if python 
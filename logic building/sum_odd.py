# to print sum of all odd natural numbers

def odd_sum(n):
    total = 0
    for i in range(1,n+1):
        if i% 2 != 0:
            total+=i
    print(total)
        
odd_sum(100)


# for i in range(1,n+1,2) this can also be used instrad of if 
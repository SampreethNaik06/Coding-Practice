# to find all the sum of elements in a array 

def array_sum(n):
    arr = []
    total = 0
    for i in range(n):
        arr.append(i)

        total = total+i
    return total

print(array_sum(5))
# Find the sum of even elements only

def sum_even(n,element):
    arr = []
    arr = element
    total = 0

    for i in range(n):
        if arr[i] % 2 == 0:
            total = total + arr[i]

    return total

print(sum_even(5,[1,10,5,4,10]))

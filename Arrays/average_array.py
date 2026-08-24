# to find the average of elements in a array
def average_array(n):
    arr = []
    total = 0

    for i in range(n):
        arr.append(i)
        total = total + i

    average = total / n
    return average

print(average_array(5))


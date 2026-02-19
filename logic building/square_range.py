# to print square numbers from 1 to n

def square(n):
    result = []
    for i in range(1, n + 1):
        result.append(i * i)
    return result

print(square(20))

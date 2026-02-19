# to check for the cube range 

def cube(n):
    if n<= 0:
        return False
    result = []
    for i in range(1,n+1):
        result.append(i*i*i)
    return result

print(cube(3))
# to find the max element in a array without maax function 

def max_array(n):
    arr = []
    for i in range(n):
        arr.append(i)

    # to find the maximum 
    max_val = arr[0]
    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]

    print(f"max = {max_val}")
    return max_val


max_array(20)
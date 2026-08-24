# to return the index of the max element

def max_array(n):
    arr = []

    for i in range(n):
        arr.append(i)
        
    max_val = arr[0]
    max_index = 0

    for i in range(1, n):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i

    print(f"max = {max_val}, at index {max_index}")

    return max_index


max_array(20)
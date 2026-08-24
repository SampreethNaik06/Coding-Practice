# to find the index of the minimum element in the array

def min(n,element):
    arr =[]
    arr = element
    min = arr[0]
    min_index = 0
    for i in range(1,n):
        if arr[i] <min:
            min = arr[i]
            min_index = i

    print(f"min = {min} at {min_index}")
    return min

min (5,[10,12,1,45,90])
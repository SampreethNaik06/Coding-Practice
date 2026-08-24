# to find the minimum element in the array 

def min(n,element):
    arr =[]
    arr = element
    min = arr[0]
    for i in range(1,n):
        if arr[i] <min:
            min = arr[i]

    print(f"min = {min}")
    return min

min (5,[10,12,1,45,90])

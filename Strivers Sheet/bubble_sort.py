# sorting using bubble sort 

def bubble_sort():
    arr = [4,5,1,3,9,0,1,3,5,6,]

    n = len(arr)

    for i in range(n):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

    return arr

print(bubble_sort())

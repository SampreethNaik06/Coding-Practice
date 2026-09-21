# function to sort a array using selection sort

def selection_sort():
    arr = [4,5,1,3,9,0,1,3,5,6,]
    n = len(arr)

    for i in range(n):
        for j in range(n):
            if arr[i]<arr[j]:
                # temp = arr[i]
                # arr[i] = arr[j]
                # arr[j] = temp
                arr[i],arr[j] = arr[j],arr[i]  # here swapping can also take place withiut temp 
    print(arr)


selection_sort()

"""
alternative way of solving selection sort is 

n = len(arr)

for i in range(n-1):
    for j in range(i+1,n)

"""



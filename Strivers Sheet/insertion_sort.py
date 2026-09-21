# code for insertion sort 

def insertion_sort(arr):
    n = len(arr)

    for i in range(1,n):
        j = i 
        while j>0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j = j-1

    return arr 


numbers = [3,1,3,5,8,9,5,3,5]
print(insertion_sort(numbers))
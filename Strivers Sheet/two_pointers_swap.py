 # function to swap an  array using two pointers

def rev_array():
    arr = [2,4,5,7,9,8,4,3,5]
    l = 0
    r = len(arr) -1

    if l <= r:
        arr[l],arr[r] = arr[r],arr[l]

        l+=1
        r-=1

    print(arr)
    return 
    

rev_array()
        



""" can also be written as  
    using single variable 
    while (i >= n//2):
        arr[i], arr[n-i-1] = arr[n-i-1],arr[i]
        i+=1
    return arr

"""
# Check if all elements in an array are unique.

def check_unique(n,element):
    arr = []
    arr = element

    for i in range(n):
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                print("no unique elements")
                return

            
    print("contains duplicates")

    return 


check_unique(5,[1,10,5,4,10])
# to find the first and the last occursncesin a array 

def first_last_occurance(n,element):
    arr = []
    arr = element

    first = -1
    last = -1

    key  = 10 

    for i in range(n):
        if arr[i] == key:
            if (first ==-1):
                first = i

            last = i


    print(first)
    print(last)


first_last_occurance(5,[1,10,5,4,10])

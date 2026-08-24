#Count how many elements are positive, negative, or zero.

def integer(n, element):
    arr = []
    arr = element

    pos_count = 0
    neg_count = 0
    zero_count = 0

    for i in range(n):
        if  arr[i] < 0:
            neg_count+=1
        elif arr[i] > 0:
            pos_count+=1
        else:
            zero_count +=1
    print(f"pos count = {pos_count}, neg count = {neg_count}, zero = {zero_count}")

    return
integer(5,[1,2,-1,0,0])

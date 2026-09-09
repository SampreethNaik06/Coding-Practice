# this program is to find all the duplicate numbers in a array 

def HashArray(arr,n):

    hash = [0] * 13 
    for i in range(len(arr)):
        hash[arr[i]] += 1

    print(hash[n])

HashArray([1,2,3,6,7,2,1,3,12],1)

# here arr is a list 
# if we want to use a array then we acan use  hash [] = array.array('i',[0] * 13 )

""" 'i' → signed integer (usually 32-bit, like int in C/C++)

'I' → unsigned integer

'f' → floating point (like float)

'd' → double precision float (like double)

'b' → signed char (8-bit)

'B' → unsigned char (8-bit) """

# neetcode used a hashset instead of hasharray  and there if there is mote than 1 occurance of the element in the array, we need to print true 

"""
def duplicate_neetcode(nums):
    hashset = set()

    for i in nums:
        if i in hashset:
            print True
        hashset.append(i)
    return False


Here basically saying it as a hashset he has actually used a set which holds only distinct elements 
"""

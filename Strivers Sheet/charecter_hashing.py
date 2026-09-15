# hashing charecters using ascii value

def charecter_hashing(s, n):
    hash = [0] * 26
    for i in range(len(s)):
        hash[ord(s[i]) - ord('a')] += 1
    print(f"{hash[ord(n) - ord('a')]}")

charecter_hashing("abshshefhsvsbaasads", "a")

"""
def charecter_hashing_all_ascii(s, n):
    hash = [0] * 256
    for ch in s:
        hash[ord(ch)] += 1
    print(hash[ord(n)])
"""


"""
Here hashing is done using hash arrays but if the number exceeds 10^9 then we cant use hasharrays 
then we use hashmap

def charecter_hashing(s,n):
    hsahmap = {}
    for i in s:
        if i in hashmap:
            hashmap[i]+=1
        else:
             hashmap[i]=1

    print(hashmap[n])

"""
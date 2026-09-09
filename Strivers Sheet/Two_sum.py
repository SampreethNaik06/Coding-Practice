
# solution for two sum using hashmap 

def hashmap(nums, target):
    map = {}

    for i, n in enumerate(nums):
        diff = target - n 
        if diff in map:
            return [map[diff], i]
        map[i] = n

    return []


print(hashmap([1, 2, 3, 4, 5], 3))

# this solution is for unsorted array 
# Count how many times a given element appears.

def count_element(arr, key):
    count = 0

    for i in range(len(arr)):
        if arr[i] == key:
            count += 1

    print(f"{key} appears {count} times")


count_element([1, 2, 4, 10, 55, 10, 10], 10)
# to check if an element is present in a array 
def is_element(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            print(f"Key element {key} is found at location {i}")
            return

    print(f"Key element {key} is not found")


is_element([1, 2, 4, 10, 55], 10)
# Program to take n integers as input into an array/list and print them

def array_display(size, element):
    arr = element

    print("Array elements are:")

    for i in range(size):
        print(arr[i], end=" ")

    print()


array_display(3, [1, 2, 3])
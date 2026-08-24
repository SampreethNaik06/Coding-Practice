
def greater_than_k(n, k):
    arr = []

    for i in range(n):
        element = int(input("Enter element: "))
        arr.append(element)

    print("Elements greater than", k, ":")

    for i in range(n):
        if arr[i] > k:
            print(arr[i], end=" ")


n = int(input("Enter number of elements: "))
k = int(input("Enter k: "))

greater_than_k(n, k)

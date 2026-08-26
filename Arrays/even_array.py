# Create a new array containing only even elements

def even_array(ele):

    arr1 = []
    arr2= []

    arr1 = ele

    for i in (arr1):
        if i %2 == 0:
            arr2.append(i)

    print(arr2)

even_array([2, 5, 8, 11, 14, 17, 20, 23, 26, 29])

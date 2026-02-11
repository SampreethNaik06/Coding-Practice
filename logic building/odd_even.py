# to chek for odd or even number
def odd_even(a,b):
    if a%2==0 and b%2==0:
        print("both are even")
    elif a%2==0 and b%2!=0:
        print("a is even and b is odd")
    elif a%2!=0 and b%2==0:
        print("a is odd and b is even")
    else:
        print("both are odd")
        
        
odd_even(2,4)
odd_even(2,3)
odd_even(3,4)
odd_even(3,5)
    

    
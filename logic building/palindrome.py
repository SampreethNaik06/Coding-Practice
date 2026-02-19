## to print a palindrome 
def palindrome(n):
    n = str(n)
    if n == (n)[::-1]:
        print("palindrome")
    else:
        print("not a palindrome")
        
palindrome(121)
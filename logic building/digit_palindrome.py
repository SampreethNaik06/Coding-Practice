#Print all numbers that are palindromes between 1–500. 

def palindrome():
    for i in range(1,500):
        if str(i) == str(i)[::-1]:
            print(i)
            
palindrome()
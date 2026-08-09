# to keep only even digits in the given number 

def  keep_even(n):
    if  n < 0 :
        print("ebter a bigger number ")
        return 
        
    result = 0 
    place = 1 
    
    while n > 0 :
        dgt = n% 10

        if dgt % 2 ==0:
            result += dgt*place
            place*=10
        n = n //10 
    print(result)
keep_even(1234567890)
        
        

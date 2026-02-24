#Print numbers between 1–100 whose digits add up to a multiple of 3. 

def mul_3():
    for i in range(1,100):
        num = i 
        digit_sum = 0
        
        while num > 0 :
            digit  = num%10
            digit_sum += digit
            num = num//10
            
        if digit_sum % 3==0:
            print(i)
            
mul_3()
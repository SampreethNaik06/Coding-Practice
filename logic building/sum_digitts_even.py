# print all the numbers whose sum of digits are even 

def sum_digits():
    for i in range(1,100):
        num = i
        digit_sum = 0
        
        while num>0:
            digit = num%10 
            digit_sum+=digit 
            num = num//10
            
        if digit_sum % 2 ==0 :
            print(i)

sum_digits()
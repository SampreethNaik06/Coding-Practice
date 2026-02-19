# to check for numbers between a and b if divisible by 7

def check_numbers(a,b):
    result = []
    for i in range(a,b):
        if i % 7 == 0 :
            result.append(i)
    return result
    
print(check_numbers(1,70))
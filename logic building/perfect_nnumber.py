# to check if a number ia a perfect number

def perfect_number(num):
    equal = 0
    
    for i in range(1, num):
        if num % i == 0:
            equal += i
            
    if num == equal:
        return True
    else:
        return False

print(perfect_number(6))


        
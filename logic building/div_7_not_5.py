# Count how many numbers between 1–500 are divisible by 7 but not by 5. 
def divisibility():
    count = 0
    
    for i in range(1, 500):
        if i % 7 == 0 and i % 5 != 0:
            count += 1
            
    return count

print(divisibility())
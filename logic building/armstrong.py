#  to check if the number is a armstrong number 

def armstrong_number(n):
    n = str(n)
    total = 0
    for i in (n):
        total += int(i)**len(n)
        
    return total

print(armstrong_number(153))
        
    
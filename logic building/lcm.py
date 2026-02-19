# lcm of two numbers using loops

def lcm(a,b):
    largest = max(a,b)
    while True:
        if largest % a == 0 and largest % b == 0:
                return largest
        largest +=1
print(lcm(12, 18))





## gcd 


def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(find_gcd(12, 18))

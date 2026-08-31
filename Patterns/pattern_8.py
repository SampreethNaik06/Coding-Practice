# 8 

def pattern_8(n):
    for i in range(n+1):

        for j in range(i):
            print(" ", end="")

        for j in range(2*n-2 * i + 1):
            print("*", end="")

        for j in range(i):
            print(" ", end="")
            
        print()

pattern_8(6)
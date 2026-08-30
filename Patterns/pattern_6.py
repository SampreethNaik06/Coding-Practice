# 6

def pattern_6(n):
    for i in range(n):
        for j in range(n,i,-1):
            print(n-j+1,end = "")

        print()

pattern_6(5)


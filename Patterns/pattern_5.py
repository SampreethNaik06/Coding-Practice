# 5

def pattern_5(n):
    for i in range(n):
        for j in range(n,i,-1):
            print("*",end = "")

        print()

pattern_5(6)
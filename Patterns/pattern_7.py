# 7
def pattern_7(n):
    for i in range(n):

        for j in range(n - i - 1):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        for j in range(n - i - 1):
            print(" ", end="")
            
        print()

pattern_7(5)
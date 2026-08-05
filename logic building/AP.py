# to check if three numbers are in arithmetic progression

def ap(a,b,c):
    if b-a == c-b:
        print(f"Three numbers {a} {b} {c} are in ap")
    else:
        return False

ap(2,4,6)
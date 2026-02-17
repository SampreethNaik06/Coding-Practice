# to check if the three ualues are in geometric progression

def gp(a,b,c):
    if b/a == c/b:
        print("GP")
    else:
        print("Not GP")
        
gp(2, 4, 8)
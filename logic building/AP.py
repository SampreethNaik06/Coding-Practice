# to check if three numbers are in arithmetic progression

def ap(a,b,c):
    if b-a==c-b:
        print("thenumbers are in arithmetic progression")
    else:
        print('it is not in arithmetic progression')
ap(2, 4, 6)
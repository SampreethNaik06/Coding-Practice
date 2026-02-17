# to check if the coordinates lie in x axis or y axis
def axis(x, y):
    if x == 0 and y == 0:
        print("origin")
    elif x == 0:
        print("y axis")
    elif y == 0:
        print("x axis")
    else:
        print("not on axis")

axis(0, 0)
axis(0, 5)
axis(4, 0)
axis(3, 7)

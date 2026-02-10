# to check the range of values and print special conditions
def temperature(temp):
    if temp>-10 and temp<0:
        print("cold")
    elif temp>=0 and temp<=20:
        print("mild warm")
    elif temp>20 and temp<=40:
        print("warm")
    elif temp>40:
        print("hot")
    
temperature(62)
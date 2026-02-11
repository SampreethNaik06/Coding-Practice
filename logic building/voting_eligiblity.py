# to check for voting eligiblity 
def voting(age):
    if age<=0 or age>100:
        print("are you even a human?")
    elif age<18:
        print("you are not eligible to vote")   
    else:
        print("you are eligible to vote")
        
        
voting(17)
voting(18)
voting(0)
voting(101)

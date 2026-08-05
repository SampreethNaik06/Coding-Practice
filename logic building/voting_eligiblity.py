# to check for voting eligiblity 
def voting_criteria(age):
    if age<=0 or age>100:
        print("are you even a human?")
    elif age<18:
        print("you are not eligible to vote!!!!")   
    else:
        print("you are eligible to vote")
        
        
voting_criteria(17)
voting_criteria(18)
voting_criteria(0)
voting_criteria(101)

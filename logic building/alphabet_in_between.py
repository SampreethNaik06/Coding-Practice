# to check if the given letter is in between the two letters or not

def check_char(ch):
    if len(ch)!=1 or not ch.isalpha():
        print("invalid input")
    elif "a"<=ch<="m":
        print("letter is avaliable in between a and m")
    elif "n"<=ch<="z":
        print("letter is avaliable in between n and z")
        
check_char("b")
check_char("n")
check_char("z")
check_char("1")
# to check if the char is letter digit or special character
def check_char(char):
    if char.isalpha():
        print("the char is a letter")
    elif char.isdigit():
        print("the char is a digit")
    else:
        print("the char is a special character")
        
        
check_char('a')
check_char('5')
check_char('@')

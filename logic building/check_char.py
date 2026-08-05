# to check if the char is letter digit or special character

def check_char(ch):
    if ch.isdigit():
        print("is digit")
    elif ch.isalpha():
        print("alphabtes")
    else:
        print("special char")

check_char("wfnweiufwe")
check_char("287292")
# to check if the chracter is lower case, upper case, digit or special character
def check_character_type(char):
    if char.islower():
        return "Lower case"
    elif char.isupper():
        return "Upper case"
    elif char.isdigit():
        return "Digit"
    else:
        return "Special character"

print(check_character_type("1"))

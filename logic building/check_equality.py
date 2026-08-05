# check if the first and last digits are equal in a 4 digit number
def check_equal(num):
    num = str(num)
    if len(num) != 4:
        print("invalid input")
    if len(num) == 4:
        if num[0] == num[3]:
            print(f"first and last of {num} is equal ")
        else:
            print("you gave a shit input")
check_equal(1221)
check_equal(1234)    
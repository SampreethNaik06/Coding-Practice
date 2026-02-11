# to check if the middle number in a 3 digit number is largest smallest or neither
def middle_number(num):
    num_ = str(num)
    if len(num_) != 3:
        print("invalid input")
    elif int(num_[1]) > int(num_[0]) and int(num_[1]) > int(num_[2]):
        print("middle number is largest")
    elif int(num_[1]) < int(num_[0]) and int(num_[1]) < int(num_[2]):
        print("middle number is smallest")
    else:
        print("middle number is neither largest nor smallest")
        
middle_number(123)
middle_number(321)
middle_number(132)
middle_number(12)

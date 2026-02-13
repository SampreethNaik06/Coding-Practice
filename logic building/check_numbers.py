# to prntthe numbers
words = ["Zero", "One", "Two", "Three", "Four",
         "Five", "Six", "Seven", "Eight", "Nine"]
for i in range(10):
    print(words[i])



## another code 

def check_num(n):
    numbers= ["Zero", "One", "Two", "Three", "Four",
              "Five", "Six", "Seven", "Eight", "Nine"]
    if 0<= n < 10:
        print(numbers[n])
    else:
        print("number is out of range")
check_num(5)

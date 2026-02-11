## to check the number of distinct 3 numbers
def distinct(num):
    number = str(num)
    for i in range(len(number)):
        for j in range(i+1,len(number)):
            if number[i] == number[j]:
                print("not distinct")
                return  # Exit early if a duplicate is found
    print("distinct")
                
distinct(123)
distinct(122)
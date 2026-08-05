# print numbers in words

def num_in_words(num):
    if num<0:
        print("num<0, not considererd")
    return
    
    numbers = ["one","two","three","four","five","six","seven","eight","nine"]
    for i in str(num):
        print(numbers[int(i)],end = "")
        
num_in_words(100)
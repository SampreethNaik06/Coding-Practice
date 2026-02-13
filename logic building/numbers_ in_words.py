# print numbers in words
def number_in_words(num):
    if num < 0:
        print("negative numbers are not allowed")
        return

    numbers = ["zero","one","two","three","four",
               "five","six","seven","eight","nine"]

    for digit in str(num):
        print(numbers[int(digit)], end=" \n")

number_in_words(123)
number_in_words(405)


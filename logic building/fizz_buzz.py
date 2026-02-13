# FizzBuzz logic

def fizz_buzz(n):
    if n%3 ==0 and n% 5 == 0:
        print("FizzBuzz")
    elif n%3 == 0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print("the number is not divisible by 3 or 5")
fizz_buzz(3)
fizz_buzz(5)
fizz_buzz(15)
fizz_buzz(7)

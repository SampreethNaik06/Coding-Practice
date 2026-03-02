##  not yet started 


# there are three laws in recursion (never forget these laws)
"""  
1. never forget base case 
2. the function should call itself with a smaller input 
3. eachcall should move the function closer to the base case 
"""



# eg count from 5 to 1 backwards using revursion 

def countdown(n):
    if  n==0:
        return 
    print(n)
    countdown(n-1)


countdown(5)

# count from 1 to 5 with recursion 

def countup(n):
    if n==0:
        return
    countup(n-1)
    print(n)

countup(5)




# # Find sum of [1, 2, 3, 4, 5]

def my_sum(lst):
    if len(lst) == 0:       # base case
        return 0
    return lst[0] + my_sum(lst[1:])

print(my_sum([1, 2, 3, 4, 5]))  



# power and base using recursion 

def power(base,exp):
    if exp==0:
        return 1
    return base * power(base,exp-1)

print(power(2,3))

# sum of numbers using recursion 

def sum_digits(n):
    if n ==0:
        return 0
    return n%10 + sum_digits(n//10)

print(sum_digits(12345))
print(sum_digits(9))



# reverse string using recursion 

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1:]) + s[0]


print(reverse("hello"))


# to find max number in a list using recursion 

def max_num(lst):
    if len(lst) == 1:      # ✅ One element = that IS the max
        return lst[0]
    return max(lst[0], max_num(lst[1:]))

print(max_num([1, 2, 3, 4, 5]))



# fibonacci sequence


def fib(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

print(fib(5))

# Find all elements greater than x

def find_greater(lst, x):
    if lst == []:        # base case — nothing left
        return []
    
    if lst[0] > x:
        return [lst[0]] + find_greater(lst[1:], x)  # keep it
    else:
        return find_greater(lst[1:], x)             # skip it
# Write a function digital_root(n) that takes a positive integer n and repeatedly replaces it with the sum of its digits until n becomes a single-digit number (0 through 9).

def digital_root(n):
    if n < 0:
        print("enter a positive number ")
        return

    count = 0 

    while n >= 10:
        digit_sum = 0
        for i in str(n):
            digit_sum += int(i)
        
        n = digit_sum
        count += 1
        print(f"step {count}: {n}")

    print(f"total steps = {count}")


digital_root(1234)
# Find the count of prime numbers in the array.

def count_prime(n, ele):
    arr = ele
    count = 0

    for j in range(n):
        num = arr[j]

        if num < 2:
            continue

        is_prime = True

        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

    return count


print(count_prime(5, [2, 4, 7, 9, 11]))


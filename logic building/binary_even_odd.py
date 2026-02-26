# Print all numbers from 1–n whose binary representation has an even number of 1s


def even_ones_binary(n):
    for i in range(1, n + 1):
        if bin(i).count('1') % 2 == 0:
            print(i, '->', bin(i)[2:])

even_ones_binary(20)
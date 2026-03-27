# 5. *Recursive Multiply*:#
# Write a recursive function to multiply two positive integers without using the * operator. You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations.

def recursiveMultiply(a, b):
    return multiply(a, b, 0, 0)

def multiply(a, b, n, total):
    if b == n:
        return total

    total += a
    return multiply(a, b, n + 1, total)
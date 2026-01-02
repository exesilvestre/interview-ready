# 1. *Is Unique*:

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(str: str)-> bool:
    chars = set()

    for i in str:
        if i in chars:
            return False
        chars.add(i)

    return True
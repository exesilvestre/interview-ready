# 1. *Is Unique*:

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(str: str)-> bool:
    chars = set()

    for i in range(len(str)):
        if str[i] in chars:
            return False
        chars.add(str[i])    
    return True
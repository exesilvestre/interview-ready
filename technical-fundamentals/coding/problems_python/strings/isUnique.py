# 1. *Is Unique*:

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(str: str)-> bool:
    aux_dict = set()
    for s in str:
        if s in aux_dict:
            return False
        aux_dict.add(s)
    return True

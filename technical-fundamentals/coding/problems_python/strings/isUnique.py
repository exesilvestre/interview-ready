# 1. *Is Unique*:

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def is_unique(str: str)-> bool:
    aux_dict = set()

    for i in str:
        if i in aux_dict:
            return False
        aux_dict.add(i)
    
    return True

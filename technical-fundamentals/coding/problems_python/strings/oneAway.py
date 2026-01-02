# 5. *One Away*#
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def isOneAway(str1: str, str2: str)-> bool:
    
    if abs(len(str1) - len(str2)) > 1:
        return False
    
    p1 = 0
    p2 = 0
    one_diff = False

    while p1 < len(str1) and p2 < len(str2):

        if str1[p1] == str2[p2]:
            p1 += 1
            p2 += 1
            continue

        if one_diff:
            return False
        
        if len(str1) == len(str2):
            p1 += 1
            p2 += 1
            one_diff = True
        elif len(str1) > len(str2):
            p1 += 1
            one_diff = True
        else:
            p2 += 1
            one_diff = True

    return True
# 5. *One Away*#
# There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.

def isOneAway(str1: str, str2: str)-> bool:

    if abs(len(str1) - len(str2)) > 1:
        return False
    
    p = 0
    q = 0
    different_flag = False

    while p < len(str1) and q < len(str2):
        if str1[p] == str2[q]:
            p +=1
            q += 1
            continue
        else:
            if different_flag:
                return False
            different_flag = True



        if len(str1) == len(str2):
            p += 1
            q += 1
        elif len(str1) > len(str2):
            p += 1
        else:
            q += 1

    if (p  < len(str1) or q < len(str2)) and different_flag:

        return False
    
    return True
# 2. *Check Permutation*:

# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutations(s1: str, s2: str) ->bool:
    if len(s1) != len(s2):
        return False
    aux_s1 = {}

    for i in s1:
        if i not in aux_s1:
            aux_s1[i] = 1
        else:
            aux_s1[i] += 1
    
    for j in s2:
        if j not in aux_s1:
            return False
        if aux_s1[j] == 0:
            return False
        aux_s1[j] -= 1
    
    return True
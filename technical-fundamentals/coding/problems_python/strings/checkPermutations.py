# 2. *Check Permutation*:

# Given two strings, write a method to decide if one is a permutation of the other.

def checkPermutations(s1: str, s2: str) ->bool:
    aux_dict = {}
    if len(s1) != len(s2):
        return False

    for i in range(len(s1)):
        if s1[i] in aux_dict:
            aux_dict[s1[i]] += 1
        else:
            aux_dict[s1[i]] = 1   

    
    for j in range(len(s2)):
        if s2[j] not in aux_dict or aux_dict[s2[j]] == 0:
            return False
        else:
            aux_dict[s2[j]] -= 1

    
    return True
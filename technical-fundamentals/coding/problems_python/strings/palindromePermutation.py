# 4. *Palindrome Permutation*:#
# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.
# ```
# EXAMPLE
# Input: Tact Coa
# Output True (permutations: "taco cat", "atco cta", etc.)
# ```

def palindromePermutation (str: str) -> bool:
    aux_dict= {}
    one_odd = False
    str = str.lower()

    for i in range(len(str)):
        if str[i] == " ":
            continue
        if str[i] in aux_dict:
            aux_dict[str[i]] += 1
        else:
            aux_dict[str[i]] = 1
    
    for  value in aux_dict.values():
        if (value % 2) != 0:
            if one_odd:
                return False
            one_odd = True
        
    return True

        
        


    


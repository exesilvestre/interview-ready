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
    
    aux_dict = {}
    odd = False
    
    for i in range(len(str)):
        if str[i] == " ":
            continue
        c = str[i].lower()
        if c in aux_dict:
            aux_dict[c] += 1
        else:
            aux_dict[c] = 1

    for i in aux_dict.values():
        if i % 2 != 0:
            if odd:
                return False
            odd = True
    
    return True
        
        


    


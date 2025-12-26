# 3.  URLify:

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

def URLify (s1 : str) -> str:
    new_str = ''
    for i in range(len(s1)):
        if s1[i] == ' ':
            new_str += "%20"
            continue
        
        new_str += s1[i]
    
    return new_str
# 3.  URLify:

# Write a method to replace all spaces in a string with '%20'.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string.

def URLify (s1 : str) -> str:
    new_str = ""
    for i in s1:
        if i == " ":
            new_str += "%20"
        else:
            new_str += i
    
    return new_str
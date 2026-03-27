# 6. *String Compression*#
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3,
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression (s: str) -> str:
    if len(s) == 0:
          return ""
    current = s[0]
    count_current = 0
    new_str = ""
    for i in s:
        if i == current:
            count_current += 1 
            continue
        else:
            new_str += (current + str(count_current))
            current = i
            count_current = 1

    new_str += (current + str(count_current))

    return new_str if len(new_str) < len(s) else s
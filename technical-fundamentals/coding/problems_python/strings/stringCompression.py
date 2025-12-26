# 6. *String Compression*#
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, the string aabcccccaaa would become a2blc5a3,
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).

def stringCompression (s: str) -> str:
    if len(s) == 0:
        return s
    compressed = ""
    counter = 1
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            compressed += s[i - 1] + str(counter)
            counter = 0
        counter += 1

    
    compressed += s[-1] + str(counter)

    if len(compressed) >= len(s):
        return s

    return compressed
# 7.Permutations without Dups: Write a method to compute all permutations of a string of unique characters.

def permutationsWithoutDups(input): 
    if len(input) == 0:
        return [""]
    if len(input) == 1:
        return [input]
    
    first = input[0]
    rest = input[1:]
    prevs = permutationsWithDups(rest)
    result = []

    for sub in prevs:
        for i in range(len(sub) + 1):
            new = sub[:i] + first + sub[i:]
            result.append(new)
        
    return result



# *Permutations with Dups*: Write a method to compute all permutations of a string whose characters are not necessarily unique. The list of permutations should not have duplicates.

def permutationsWithDups(input):
    results = set()
    permutations(input, "", results)
    return list(results)


def permutations(remaining, path, results):
    if len(remaining) == 0:
        results.add(path)
        return
    for i in range(len(remaining)):
        permutations(remaining[:i] + remaining[i + 1:], path + remaining[i], results)
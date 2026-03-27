# 4. *Power Set*:#
# Write a method to return all subsets of a set#
# Example 
# Input: [1, 2, 3]
# Output: [ [], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3] ];


def powerSet(set):
    if len(set) == 0:
        return [[]]
    
    if len(set) == 1:
        return [[], [set[0]]]

    previous_set = powerSet(set[1:])
    result = []
    for subset in previous_set:
        result.append(subset)
        result.append([set[0]] + subset)
    
    return result
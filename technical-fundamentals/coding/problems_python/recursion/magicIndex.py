from typing import List, Optional

# 3. Magic Index
# A magic index in an array A[0...n-1] is defined to be an index such that A[i] = i.
# Given a sorted array of distinct integers, find a magic index, if one exists.

def find_magic_index_distinct(arr: List[int]) -> Optional[int]:
    return findMagic(arr, 0, len(arr) -1)


def findMagic(array, start, end):
    if start > end:
        return None
    
    pivot_index = (start + end) // 2
    pivot = array[pivot_index]
    if pivot_index == pivot:
        return pivot
    
    elif pivot > pivot_index:
        return findMagic(array, start, pivot_index - 1)
    else:
        return findMagic(array, pivot_index + 1, end)

def find_magic_index_non_distinct(arr: List[int]) -> Optional[int]:
    return search(arr, 0, len(arr) - 1)



def search(array, start, end):
    if start > end:
        return None
    
    pivot_index = (start + end) // 2
    pivot = array[pivot_index]

    if pivot_index == pivot:
        return pivot
    
    left_index = min(pivot_index - 1, pivot)
    left = search(array, start, left_index)
    if left is not None:
        return left
    
    right_index = max(pivot_index + 1, pivot)
    return search(array, right_index, end)
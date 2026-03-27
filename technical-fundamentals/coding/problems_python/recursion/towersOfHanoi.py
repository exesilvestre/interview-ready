# 6. *Towers of Hanoi*#
# In the classic problem of the Towers of Hanoi, you have 3 towers and
# N disks of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom
# (i.e., each disk sits on top of an even larger one).
#
# You have the following constraints:
# Only one disk can be moved at a time.
# A disk is slid off the top of one tower onto another tower.
# A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.

type Tower = list[int]

def towersOfHanoi(n: int):
    a = list(range(n, 0, -1))
    b = []
    c = []
    hanoi(n, a, b, c)
    return (a, b, c)


def hanoi(n, a: Tower, b:Tower, c: Tower):
    if n == 1:
        c.append(a.pop())
        return [a, b, c]
    
    if n == 2:
        b.append(a.pop())
        c.append(a.pop())
        c.append(b.pop())
        return [a, b, c]

    hanoi(n - 1, a, c, b)
    c.append(a.pop())
    hanoi(n - 1, b, a, c)

    return [a, b, c]

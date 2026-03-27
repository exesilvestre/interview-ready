# 1. *Triple Step*#
# A child is running up a staircase with n steps and can hop either
# 1 step, 2 steps, or 3 steps at a time. Implement a method to count
# how many possible ways the child can run up the stairs.
#


def tripleSteps(n: int):
    if n <= 0:
        return 0
    
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return tripleSteps(n - 1) + tripleSteps(n - 2) + tripleSteps(n - 3)
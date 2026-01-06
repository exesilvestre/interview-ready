# 2. *Stack Min*: How would you design a stack which,
# in addition to push and pop,
# has a function min which returns the minimum element?
# Push, pop, and min should all operate in O(1) time.

# 1. *Three in One*: Describe how you could use a single array to implement three stacks.


class StackMin:
    def __init__(self):
        self.array = []
        self.mins = []


    def push(self, value):
        self.array.append(value)
        if not self.mins or value <= self.mins[-1]:
            self.mins.append(value)
        return value

    def pop(self):
        if not self.mins:
            return None
        pop = self.array.pop()
        if pop == self.mins[-1]:
            self.mins.pop()
        return pop


    def min(self):
        if not self.mins:
            return None
        return self.mins[-1]




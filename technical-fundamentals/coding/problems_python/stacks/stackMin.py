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
        if not self.mins or self.mins[-1] >= value:
            self.mins.append(value)
        self.array.append(value)
        

    def pop(self):
        if not self.array:
            return None
        value = self.array.pop()
        if value == self.mins[-1]:
            self.mins.pop()
        return value
        


    def min(self):
        if not self.mins:
            return None
        return self.mins[-1]






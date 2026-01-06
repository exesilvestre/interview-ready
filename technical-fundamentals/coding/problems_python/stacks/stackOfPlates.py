# 3. *Stack of Plates*#
# Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack
# exceeds some threshold. Implement a data structure SetOfStacks that mimics this.
# SetOfStacks should be composed of several stacks and should create a new stack once
# the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave
# identically to a single stack (that is, pop() should return the same values as it would if
# there were just a single stack)#
# FOLLOW UP: Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.

class StackOfPlates:
    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity

    
    def push(self, value: int):
        if not self.stacks or len(self.stacks[-1]) == self.capacity:
            self.stacks.append([])
        self.stacks[-1].append(value)

    
    def pop(self):
        if not self.stacks:
            return None
        value = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return value
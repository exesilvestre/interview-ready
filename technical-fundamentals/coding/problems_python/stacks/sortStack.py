# 5. *Sort Stack*#
# Write a program to sort a stack such that the smallest items are on the top.
# You can use an additional temporary stack, but you may not copy the elements
# into any other data structure (such as an array).
# The stack supports the following operations: push, pop, peek, and isEmpty.

class SortStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        if self.isEmpty():
            self.stack.append(value)
            return
        aux_stack = []
        while self.stack and self.stack[-1] < value:
            aux_stack.append(self.stack.pop())
        
        self.stack.append(value)
        while aux_stack:
            self.stack.append(aux_stack.pop())


    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()


    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]


    def isEmpty(self):
        return len(self.stack) == 0


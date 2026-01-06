# 4. *Queue via Stacks*#
# Implement a MyQueue class which implements a queue using two stacks.

class MyQueue:
    def __init__(self):
        self.right = []
        self.left = []


    def enqueue(self, value):
        self.right.append(value)
        


    def dequeue(self):
        if self.isEmpty():
            return None
        if not self.left:
            self.move_left()
        value = self.left.pop()
        
        return value




    def peek(self):
        if self.isEmpty():
            return None
        if not self.left:
            self.move_left()
        return self.left[-1]





    def isEmpty(self):
        return len(self.right) == 0 and len(self.left) == 0



    def move_left(self):
        while self.right:
            self.left.append(self.right.pop())




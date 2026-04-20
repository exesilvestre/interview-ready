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
            self.moveLeft()
        return self.left.pop()


    def peek(self):
        if self.isEmpty():
            return None
        
        if not self.left:
            self.moveLeft()
        
        return self.left[-1]

  
    def isEmpty(self):
        return not self.right and not self.left

    def moveLeft(self):
        while self.right:
            self.left.append(self.right.pop())




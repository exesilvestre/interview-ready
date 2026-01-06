# 1. *Three in One*: Describe how you could use a single array to implement three stacks.


class ThreeStacks:
    def __init__(self, array_length: int):
        self.array_length = array_length
        self.array = [None] * array_length
        self.stack_length = array_length // 3
        self.tops = [-1]*3

    def push(self, stack_num: int, value):
        if stack_num < 0 or stack_num > 2:
            return None
        if self.tops[stack_num] + 1 >= (self.stack_length):
            return None
        self.tops[stack_num] += 1
        index = self.tops[stack_num] + stack_num * self.stack_length
        self.array[index] = value
        

    def pop(self, stack_num: int):
        if stack_num < 0 or stack_num >2:
            return None
        
        if self.tops[stack_num] == -1:
            return None
        
        index = self.tops[stack_num] + stack_num * self.stack_length
        value = self.array.pop(index)
        self.tops[stack_num] -= 1
        return value

    def peek(self, stack_num: int):
        if stack_num < 0 or stack_num > 2:
            return None
    
        if self.tops[stack_num] == -1:
            return None
        index = self.tops[stack_num] + stack_num * self.stack_length
        return self.array[index]

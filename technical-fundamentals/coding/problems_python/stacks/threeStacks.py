# 1. *Three in One*: Describe how you could use a single array to implement three stacks.


class ThreeStacks:
    def __init__(self, array_length: int):
        self.array = [None] * array_length
        self.stack_length = array_length // 3
        self.tops = [-1] * 3
        self.array_length =array_length

    def push(self, stack_num: int, value):
        if stack_num < 0 or stack_num > 2:
            return None
        
        if self.tops[stack_num] + 1 >= self.stack_length:
            return None
        
        self.tops[stack_num] += 1
        index = self.tops[stack_num] + self.stack_length * stack_num
        self.array[index] = value



    def pop(self, stack_num: int):
        if stack_num < 0 or stack_num > 2:
            return None
        
        if self.tops[stack_num] == -1:
            return None
        
        index = self.tops[stack_num] + self.stack_length * stack_num
        pop = self.array[index]
        self.tops[stack_num] -= 1
        self.array[index] = None
        return pop

    def peek(self, stack_num: int):
        if stack_num < 0 or stack_num > 2:
            return None
    
        if self.tops[stack_num] == -1:
            return None
        index = self.tops[stack_num] + stack_num * self.stack_length
        return self.array[index]

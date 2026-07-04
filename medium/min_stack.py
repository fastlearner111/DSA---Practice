#Design a stack that supports push, pop, top, and retrieving 
#the minimum element in O(1) time.
#
#MinStack()    → initialize
#push(val)     → push val onto stack
#pop()         → remove top element  
#top()         → get top element without removing
#getMin()      → retrieve minimum element in O(1)
#
#Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
#        [[],[-2],[0],[-3],[],[],[],[]]
#Output: [null,null,null,null,-3,null,0,-2] 


#Pattern - Stack
#  Approach - the key insight: use TWO stacks. One main stack for all values. 
# One min stack that tracks the current minimum at each level.
# When you push — also push the current minimum to the min stack. When you pop — pop from both.
# Data Strucutre --two lists, not dict.
# Big O -- O(1) for all operations, O(n) space.

class MinStack:
    def __init__(self):

        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if self.minStack:
            current_min = min(val, self.minStack[-1])
        else:
            current_min = val
        self.minStack.append(current_min)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getmin(self):
        return self.minStack[-1]

s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getmin())
s.pop()
print(s.top())
print(s.getmin())


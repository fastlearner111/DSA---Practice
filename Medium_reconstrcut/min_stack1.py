#Design a stack that supports:
#
#MinStack()     — initialize the stack
#push(val)      — push val onto the stack
#pop()          — remove the top element
#top()          — get the top element without removing it
#getMin()       — retrieve the minimum element in O(1) time
#
#All operations must run in O(1) time.
#
#Input:  ["MinStack","push","push","push","getMin","pop","top","getMin"]
#        [[],[-2],[0],[-3],[],[],[],[]]
#
#Step by step:
#MinStack()  → initialize
#push(-2)    → stack: [-2]
#push(0)     → stack: [-2, 0]
#push(-3)    → stack: [-2, 0, -3]
#getMin()    → return -3
#pop()       → remove -3, stack: [-2, 0]
#top()       → return 0
#getMin()    → return -2
#
#Output: [null,null,null,null,-3,null,0,-2]

# Pattern - Stack
# Approach - 
# data Strucuture - dict
# big O - 

class MyStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self,val):
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
    
    def getMin(self):
        return self.minStack[-1]


s = MyStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.getMin())
s.pop()
print(s.top())
print(s.getMin())

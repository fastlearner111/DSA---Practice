#Design a stack that supports the following operations in O(1) time:
#
#MinStack()     — initialize the stack object
#push(val)      — push val onto the stack
#pop()          — remove the top element from the stack
#top()          — get the top element without removing it
#getMin()       — retrieve the minimum element in the stack
#
#All operations must run in O(1) time.
#
#Step by step:
#MinStack()   → initialize
#push(-2)     → stack: [-2],      min: [-2]
#push(0)      → stack: [-2,0],    min: [-2,-2]
#push(-3)     → stack: [-2,0,-3], min: [-2,-2,-3]
#getMin()     → return -3
#pop()        → remove -3
#top()        → return 0
#getMin()     → return -2
#
#Output: [null,null,null,null,-3,null,0,-2]

class MyStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self,val):
        self.stack.append(val)
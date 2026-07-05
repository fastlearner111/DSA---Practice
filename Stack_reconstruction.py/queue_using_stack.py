#Implement a first-in-first-out (FIFO) queue using only two stacks.
#The implemented queue should support:
#
#- push(x): pushes element x to the back of the queue
#- pop(): removes and returns the element from the front of the queue
#- peek(): returns the element at the front without removing it
#- empty(): returns True if the queue is empty, False otherwise
#
#Input:  ["MyQueue","push","push","peek","pop","empty"]
#        [[],[1],[2],[],[],[]]
#Output: [null,null,null,1,1,false]
#
#Constraints:
#- You may only use standard stack operations (push to top, peek/pop from top, size, is empty)
#- Must implement using exactly two stacks

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self,x):
        self.stack1.append(x)
    
    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    
    def empty(self):
        return  len(self.stack1) == 0 and len(self.stack2) == 0
    
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())
        

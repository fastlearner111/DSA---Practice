#Implement a first-in-first-out (FIFO) queue using only two stacks.
#
#Implement the MyQueue class:
#- push(x): pushes element x to the back of the queue
#- pop(): removes and returns the element from the front
#- peek(): returns the element at the front without removing it
#- empty(): returns True if the queue is empty, False otherwise
#
#Input:
#["MyQueue","push","push","peek","pop","empty"]
#[[],[1],[2],[],[],[]]
#Output: [null,null,null,1,1,False]

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
        return not self.stack1 and not self.stack2
    

q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())
print(q.pop())
print(q.empty())

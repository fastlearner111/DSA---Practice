#Implement a last-in-first-out (LIFO) stack using only one or two queues.
#The implemented stack should support the following operations:
#
#- push(x): pushes element x to the top of the stack
#- pop(): removes and returns the element on top of the stack
#- top(): returns the element on top without removing it
#- empty(): returns True if the stack is empty, False otherwise
#
#input = ["MyStack", "push", "push", "top", "pop", "empty"]
#[[], [1], [2], [], [], []]
#Output: [null, null, null, 2, 2, False]

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):                       #3# def push(slef,x): self.q.append(x) for i in range(self.q) - 1)
        self.q.append(x)                      # self.q.append(self.q.popleft())
        for i in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        if self.isEmpty():
            raise Exception("stack is already empty!. cannot do pop operation")
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("stack is empty!. cannot top value of stack.")
        return self.stack[-1]

"""
Implementing Queue using Two Stacks.
stack1 -> used to enqueue.
stack2 -> used to dequeue.
while performing dequeue.
  - we shift all items from stack1 to stack2 only if stack2 is empty..

Time Complexity:
-> enqueue() O(1)
-> dequeue() O(N)
-> isEmpty() O(1)
-> peek()    O(N)
"""

class Queue:

    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, data):
        self.stack1.push(data)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Invalid operation. Queue is already empty!")
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Invalid operation. Queue is already empty!")
        if self.stack2.isEmpty():
            while not self.stack1.isEmpty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.peek()

    def isEmpty(self):
        return self.stack1.isEmpty() and self.stack2.isEmpty()


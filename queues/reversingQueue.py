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


class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue is already empty!.")
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is already empty!.")
        return self.queue[0]

    def reverseQueue(self):
        stack = Stack()
        while not self.isEmpty():
            valueAtFront = self.dequeue()
            stack.push(valueAtFront)
        while not stack.isEmpty():
            valueAtTop = stack.pop()
            self.enqueue(valueAtTop)

    def printQueue(self):
        print(f"FRONT -> {self.queue}")

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


def reverseString(s: str):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    reversedString = ''

    while not stack.isEmpty():
        reversedString += stack.pop()

    return reversedString

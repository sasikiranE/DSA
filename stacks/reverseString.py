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


def reverseString(s: str):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    reversedString = ''

    while not stack.isEmpty():
        reversedString += stack.pop()

    return reversedString

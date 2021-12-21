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


def checkBalancedParentheses(s: str):
    stack = Stack()

    val = {
        '(': 1, '[': 2, '{': 3,
        ')': -1, ']': -2, '}': -3
    }

    for ch in s:
        if val[ch] > 0:
            stack.push(ch)
        else:
            if stack.isEmpty():
                return False
            top = stack.pop()
            if val[top] + val[ch] != 0:
                return False

    return stack.isEmpty()


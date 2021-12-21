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


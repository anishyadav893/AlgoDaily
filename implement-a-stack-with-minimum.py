# This is my solution for AlgoDaily problem Implement a Stack With Minimum
# Located at https://algodaily.com/challenges/implement-a-stack-with-minimum

class MinStack:
    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val):
        self._stack.append(val)
        if len(self._minStack) == 0 or val < self._minStack[-1]:
            self._minStack.append(val)

    def pop(self):
        if len(self._stack) > 0:
            popped_ele = self._stack.pop()
            if popped_ele == self._minStack[-1]:
                self._minStack.pop()
        else:
            return

    def peek(self):
        return self._stack[-1]

    def min(self):
        return self._minStack[-1]



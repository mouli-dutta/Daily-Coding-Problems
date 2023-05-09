# Good morning! Here's your coding interview problem for today.

# This problem was asked by Amazon.

# Implement a stack that has the following methods:

# push(val), which pushes an element onto the stack
# pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
# max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
# Each method should run in constant time.


class Stack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val):
        self.stack.append(val)
        if not self.max_stack or val >= self.max_stack[-1]:
            self.max_stack.append(val)

    def pop(self):
        if not self.stack:
            raise IndexError("pop from empty stack")
        val = self.stack.pop()
        if val == self.max_stack[-1]:
            self.max_stack.pop()
        return val

    def max(self):
        if not self.stack:
            raise IndexError("max from empty stack")
        return self.max_stack[-1]

    def print(self):
        pretty_stack = ""
        for i in range(len(self.stack)-1, -1, -1):
            pretty_stack += "|" + str(self.stack[i]).center(4) + "|"
            if self.stack[i] == self.max_stack[-1]:
                pretty_stack += "  max"
            pretty_stack += "\n"
        pretty_stack += " ----"
        print(pretty_stack)


s = Stack()
s.push(2)
s.push(9)
s.push(1)
s.push(3)
s.push(7)
s.push(10)

print('stack elements:')
s.print()


s.pop()
s.pop()

print("after poping:")

s.print()




# output
# stack elements:
# | 10 |  max
# | 7  |
# | 3  |
# | 1  |
# | 9  |
# | 2  |
#  ----
# after poping:
# | 3  |
# | 1  |
# | 9  |  max
# | 2  |
#  ----
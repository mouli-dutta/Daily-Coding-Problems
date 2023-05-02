# Good morning! Here's your coding interview problem for today.

# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.


def is_balanced(str):
    table = {')' : '(', '}' : '{' , ']' : '['}
    stack = []

    for s in str:
        if s in table:
            if not stack or table[s] != stack.pop():
                return False
        else:
            stack.append(s)
    
    return not stack

# test
print(is_balanced("([])[]({})"))
print(is_balanced("([)]"))
print(is_balanced("((()"))
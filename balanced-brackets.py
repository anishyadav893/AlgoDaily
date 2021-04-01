# This is my solution for AlgoDaily problem Balanced Brackets
# Located at https://algodaily.com/challenges/balanced-brackets

def validate_symbols(s):
    stack = list()
    
    for i in s:
        if i in ['(', '[', '{']:
            stack.append(i)
        elif i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
        elif i == '}' and stack[-1] == '{':
            stack.pop()
        else:
            return False
    return len(stack) == 0
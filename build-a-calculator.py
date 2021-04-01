# This is my solution for AlgoDaily problem Build a Calculator
# Located at https://algodaily.com/challenges/build-a-calculator

def calculator(s):
    result = 0
    num_stack = []
    operator_stack = []
    sign = 1
    
    for i in range(len(s)):
        curr = s[i]
        if curr == ' ':
            continue
        elif curr == '+':
            sign = 1
        elif curr == '-':
            sign = -1
        elif curr <= '9' and curr >= '0':
            num = curr
            while i + 1 < len(s) and s[i+1] >= '0' and s[i+1] <= '9':
                num += s.charAt(i + 1)
                i += 1
            
            result += sign * int(num)
        elif curr == '(':
            num_stack.append(result)
            result = 0
            operator_stack.append(sign)
            sign = 1
        elif curr == ')':
            result = operator_stack.pop() * result + num_stack.pop()
            sign = 1
    
    return result
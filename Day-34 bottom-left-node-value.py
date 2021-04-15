# This is my solution for AlgoDaily problem Bottom Left Node Value
# Located at https://algodaily.com/challenges/bottom-left-node-value

from collections import deque

def bottom_left_node(root):
    dq = deque()
    dq.append(root)
    
    while len(dq) > 0:
        rt = dq.popleft()
        
        if rt.right:
            dq.append(rt.right)
        if rt.left:
            dq.append(rt.left)
    return rt.val
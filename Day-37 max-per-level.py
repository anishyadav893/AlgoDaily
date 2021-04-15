# This is my solution for AlgoDaily problem Max Per Level
# Located at https://algodaily.com/challenges/max-per-level

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_per_level(root):
    if not root:
        return []
    
    answer = []
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        queue_size = len(queue)
        max_value = -99999999999999
        
        for i in range(queue_size):
            curr = queue.pop(0)
            if curr.val > max_value:
                max_value = curr.val
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        answer.append(max_value)
    return answer


# root = Node(2)
# root.left = Node(3)
# root.right = Node(7)
# root.left.left = Node(5)
# root.left.right = Node(8)
# root.right.right = Node(9)
# print(maxValPerLevel(root))



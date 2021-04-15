# This is my solution for AlgoDaily problem Mean Per Level
# Located at https://algodaily.com/challenges/mean-per-level

def mean_of_levels(root):
    if not root:
        return []
      
    answer = []
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        queue_size = len(queue)
        total = 0
        
        for i in range(queue_size):
            curr = queue.pop(0)
            total += curr.val
            
            if curr.left:
                queue.append(curr.left)
            if curr.right: 
                queue.append(curr.right)
        answer.append(total / queue_size)
    
    return answer
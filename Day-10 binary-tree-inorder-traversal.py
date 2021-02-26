# This is my solution for AlgoDaily problem Binary Tree Inorder Traversal
# Located at https://algodaily.com/challenges/binary-tree-inorder-traversal

def inorder(root):
    answer = []
    
    helper_func(root, answer)
    
    return answer
  
def helper_func(root, answer):
    if root:
        if root.left:
            helper_func(root.left, answer)
        answer.append(root.val)
        if root.right:
            helper_func(root.right, answer)
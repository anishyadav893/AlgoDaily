# This is my solution for AlgoDaily problem Validate a BST
# Located at https://algodaily.com/challenges/validate-a-bst

def is_valid_bst(root):
    tree_search = []
    tree_traversal(root, tree_search)
    
    for i in range(len(tree_search) - 1):
        if tree_search[i] >= tree_search[i + 1]:
            return False
        
    return True
  
def tree_traversal(root, result):
    if root is None:
        return
    
    tree_traversal(root.left, result)
    result.append(root.val)
    tree_traversal(root.right, result)
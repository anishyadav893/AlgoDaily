# This is my solution for AlgoDaily problem Identical Trees
# Located at https://algodaily.com/challenges/identical-trees

def identical_trees(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.val == tree2.val:
        return identical_trees(tree1.left, tree2.left) and identical_trees(tree1.right, tree2.right)
      
    return False
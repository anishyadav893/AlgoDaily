# This is my solution for AlgoDaily problem String From Binary Tree
# Located at https://algodaily.com/challenges/string-from-binary-tree

def stringFromTree(tree):
    if not tree:
        return ''
    
    left = stringFromTree(tree.left)
    right = stringFromTree(tree.right)
    
    if left and right:
        return "{}[[{}][{}]]".format(tree.val, left, right)
    if left:
        return "{}[[{}]]".format(tree.val, left)
    if right:
        return "{}[[{}]]".format(tree.val, right)
    else:
        return "{}".format(tree.val)
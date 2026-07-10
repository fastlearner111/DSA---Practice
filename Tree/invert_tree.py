#Given the root of a binary tree, invert the tree
#and return its root.
#
root = [4,2,7,1,3,6,9]
##Output: [4,7,2,9,6,3,1]
##
##Input:  root = [2,1,3]
#Output: [2,3,1]
#
#Input:  root = []
#Output: []

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root):
        if not root:
            return None
        
        root.left, root.right  = invert_tree(root.right), invert_tree(root.left)
    
        return root

##Output: [4,7,2,9,6,3,1]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(invert_tree(root))
#Given the root of a binary tree, return its maximum depth.
#Maximum depth is the number of nodes along the longest path 
#from root to the farthest leaf node.

#root = [3,9,20,null,null,15,7]
#Output: 3
#
#Input:  root = [1,null,2]
#Output: 2
#
#Input:  root = []
#Output: 0

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def findDepth(root):
    if not root:
        return 0
    
    left_height = findDepth(root.left)
    right_height = findDepth(root.right)

    return 1 + max(left_height, right_height)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(findDepth(root))
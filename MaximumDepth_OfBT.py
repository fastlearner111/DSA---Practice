#Given the root of a binary tree, return its maximum depth.
#Maximum depth is the number of nodes along the longest path
#from the root node down to the farthest leaf node.
#
#root = [3,9,20,null,null,15,7]
#Output: 3
#
#Input:  root = [1,null,2]
#Output: 2

class ListTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxdepth(root):
    if not root:
        return 0
    left = maxdepth(root.left)
    right = maxdepth(root.right)
    return 1 + max(left,right)

root = ListTree(3)
root.left = ListTree(9)
root.right = ListTree(20)
root.right.right = ListTree(15)
root.right.left = ListTree(7)

print(maxdepth(root))


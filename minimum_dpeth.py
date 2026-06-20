#Return the minimum depth of a binary tree. Minimum depth
#is the number of nodes along the shortest path from root
#to the nearest leaf node.
#
#Input:  root = [3,9,20,null,null,15,7]
#Output: 2
#
#Input:  root = [2,null,3,null,4]
#Output: 5

class ListTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def mindepth(root):
    if not root:
        return 0
    if not root.left:
        return 1 + mindepth(root.right)
    if not root.right:
        return 1 + mindepth(root.left)
    return 1 + min(mindepth(root.left), mindepth(root.right))

root = ListTree(3)
root.left = ListTree(9)
root.right = ListTree(20)
root.right.left = ListTree(15)
root.left.right = ListTree(7)

print(mindepth(root))
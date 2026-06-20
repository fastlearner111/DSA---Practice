#Given a binary tree, determine if it is height-balanced.
#A height-balanced binary tree is one where the depth of the
#two subtrees of every node never differs by more than one.
#
#Input:  root = [3,9,20,null,null,15,7]
#Output: True
#
#Input:  root = [1,2,2,3,3,null,null,4,4]
#Output: False


class ListTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def height(root):
        if not root:
            return 0
        left = height(root.left)
        right = height(root.right)
        if left == -1 or right == -1:
             return -1
        if abs(left - right) > 1:
             return -1
        return 1 + max(left,right)

def isBalanced(root):
    return height(root) != -1

root = ListTree(3)
root.left = ListTree(9)
root.right = ListTree(20)
root.right.left = ListTree(15)
root.right.right = ListTree(7)

print(isBalanced(root))
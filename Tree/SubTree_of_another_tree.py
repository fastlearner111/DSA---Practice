#Given the roots of two binary trees root and subRoot, return True 
#if there is a subtree of root with the same structure and node 
#values as subRoot, and False otherwise.
#
#A subtree of a binary tree is a tree that consists of a node 
#and all its descendants.
#
root = [3,4,5,1,2]
subRoot = [4,1,2]
#Output: True
#
#Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#Output: False
#
#Constraints:
#- Number of nodes in root: [1, 2000]
#- Number of nodes in subRoot: [1, 1000]
#- -10^4 <= root.val, subRoot.val <= 10^4

class TreeNode:
    def __init__(self,val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(a,b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    
    return isSameTree(a.left, b.left) and isSameTree(a.right, b.right)

def isSubtree(root, subRoot):
    if not root:
        return False
    if isSameTree(root,subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subRoot = TreeNode(4)
subRoot.left = TreeNode(1)
subRoot.right = TreeNode(2)

print(isSubtree(root, subRoot))



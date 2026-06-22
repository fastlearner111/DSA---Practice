#Subtree of Another Tree
#Given two binary trees root and subRoot, return True if there is a subtree of root that has the same structure and node values as subRoot, and False otherwise.

root = [3,4,5,1,2]
subRoot = [4,1,2]
#Output: True
#
#Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
#Output: False

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def isSubtree(root,subRoot):
    if not root:
        return False
    if isSameTree(root,subRoot):
        return True
    #else:
     #   return False
    return isSubtree(root.left,subRoot) or isSubtree(root.right, subRoot)
    
def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


#root = [3,4,5,1,2]
#subRoot = [4,1,2]

root = TreeNode(3)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(2)

subroot = TreeNode(4)
subroot.left = TreeNode(1)
subroot.right = TreeNode(2)

print(isSubtree(root,subroot))


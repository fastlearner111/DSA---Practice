#Given the roots of two binary trees p and q, 
#return True if they are the same tree, False otherwise.
#Same means identical structure AND identical values at every node.
#
p = [1,2,3] 
q = [1,2,3]
##Output: True
##
#Input:  p = [1,2], q = [1,null,2]
#Output: False
#
#Input:  p = [1,2,1], q = [1,1,2]
#Output: False

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val 
        self.left = left
        self.right = right

def isSameTree(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)

print(isSameTree(p,q))
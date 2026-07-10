#Given a BST and two nodes p and q, return their lowest common ancestor.
#LCA is the lowest node that has both p and q as descendants.
#
#Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
#Output: 6
#
#Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
#Output: 2
#
#Input:  root = [2,1,3], p = 1, q = 3
#Output: 2

class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def lowest(root, p, q):
    curr = root

    while curr:
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        else:
            return curr

root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

p = root.left
q = root.right

print(lowest(root,p,q).val)
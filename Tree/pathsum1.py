#You are given the root of a binary tree and an integer targetSum,
#return true if the tree has a root-to-leaf path such that adding
#up all the values along the path equals targetSum.
#
#A leaf is a node with no children.
#
#Example 1:
#Input: root = [1,2,3], targetSum = 3
#Output: true
#Explanation: The root-to-leaf path with the target sum is 1 -> 2.
#
#Example 2:
#root = [-15,10,20,null,null,15,5,-5] 
targetSum = 15
#Output: true
#Explanation: The root-to-leaf path with the target sum is -15 -> 20 -> 15 -> -5.
#
#Example 3:
#Input: root = [1,1,0,1], targetSum = 2
#Output: false

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def hasPathsum(root, targetSum):
    if not root:
        return False
    
    if not root.left and not root.right:
        return targetSum == root.val
    
    remaining = targetSum - root.val

    return hasPathsum(root.left, remaining) or hasPathsum(root.right, remaining)

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

print(hasPathsum(root, 15))
#Given root of binary tree, determine if it is a valid BST.
#
#Valid BST: left subtree values < node < right subtree values.
#This must hold for every node.
#
root = [2,1,3]
#Output: True
#
#Input:  root = [5,1,4,null,null,3,6]
#Output: False  (4 is in right subtree but 4 < 5)
#
#Input:  root = [2,2,2]
#Output: False

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isvalidate(root):
    def dfs(node,low,high):
        if not node:
            return True
        
        if not (low < node.val < high):
            return False
        
        return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
    return dfs(root, float('-inf'), float('inf'))


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
print(isvalidate(root))
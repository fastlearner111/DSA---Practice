#Diameter of Binary Tree
#Given the root of a binary tree, return the diameter of the tree.
#
#The diameter of a binary tree is the length of the longest path between any two nodes.
#The path may or may not pass through the root.
#
#The length of a path is measured in number of edges, not nodes.
#root = [1,2,3,4,5]
#Output: 4
#
#Input:  root = [1,2]
#Output: 1

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def diameter(root):
    diameter = 0

    def dfs(node):
        nonlocal diameter
        if not node:
            return 0

        left_height = dfs(node.left)
        right_height = dfs(node.right)

        diameter = max(diameter, left_height + right_height)

        return 1 + max(left_height,right_height)
    
    dfs(root)
    return diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))
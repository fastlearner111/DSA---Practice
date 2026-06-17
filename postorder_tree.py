#Given the root of a binary tree, return the preorder traversal
#of its nodes' values.

root = [1,2,3]
#Output: [1,2,3]
#
#Input:  root = []
#Output: []
#
#Input:  root = [1]
#Output: [1]

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right 

def preorderTraversal(root):
    result = []
    if not root:
        return result
    result += preorderTraversal(root.left)
    result += preorderTraversal(root.right)
    result.append(root.val)
    return result

root = TreeNode(1)
root.right = TreeNode(3)
root.left = TreeNode(2)

print(preorderTraversal(root))

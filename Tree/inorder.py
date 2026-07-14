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

def inorder(root):
    result = []
    if not root:
        return result
    result += inorder(root.left)
    result.append(root.val)
    result += inorder(root.right)
    return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(inorder(root))
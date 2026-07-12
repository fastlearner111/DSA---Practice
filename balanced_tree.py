#Given a binary tree, determine if it is height-balanced.
#A height-balanced binary tree is one where the depth of the
#two subtrees of every node never differs by more than one.
#
#Input:  root = [3,9,20,null,null,15,7]
#Output: True
#
#Input:  root = [1,2,2,3,3,null,null,4,4]
#Output: False


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root):
    if not root:
        return (True, 0)
    
    left_balanced, left_height = dfs(root.left)
    right_balanced, right_height = dfs(root.right)

    balanced = (
        left_balanced and
        right_balanced and
        abs(left_height - right_height) <= 1
    )

    height = 1 + max(left_height, right_height)
    return (balanced, height)

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(dfs(root)[0])
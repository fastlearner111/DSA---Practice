
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(self,root):
    if not root:
        return []

    root.left, root.right = self.invert_tree(root.right), self.invert_tree(root.left)
    return root


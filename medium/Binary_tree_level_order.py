#Given root of binary tree, return level order traversal as list of lists.
#
#root = [3,9,20,null,null,15,7]
#Output: [[3],[9,20],[15,7]]
#
#Input:  root = [1]
#Output: [[1]]
#
#Input:  root = []
#Output: []

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def levelorder(root):
    if not root:
        return []
    
    result = []
    queue  = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)
    return result



# Build the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelorder(root))




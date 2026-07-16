#Binary Tree Level Order Traversal
#
#Given a binary tree root, return the level order traversal of
#it as a nested list, where each sublist contains the values 
#of nodes at a particular level in the tree, from left to right.
#
#Example 1:
#Input: root = [1,2,3,4,5,6,7]
#Output: [[1],[2,3],[4,5,6,7]]
#
#Example 2:
#Input: root = [1]
#Output: [[1]]
#
#Example 3
#Input: root = []
#Output: []
#

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    return result

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(levelOrder(root))
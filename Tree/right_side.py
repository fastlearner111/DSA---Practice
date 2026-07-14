#Given root of binary tree, return values of nodes you can see 
#from the right side (one value per level — the rightmost node).
#
#Input:  root = [1,2,3,null,5,null,4]
#Output: [1,3,4]
#
#Input:  root = [1,2,3,4,null,null,null,5]
#Output: [1,3,4,5]
#
#Input:  root = [1,null,3]
#Output: [1,3]
#
#Input:  root = []
#Output: []

from collections import deque

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
def rightSideView(root):
    if not root:
        return []
    
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        rightmost = None

        for _ in range(level_size):
            node = queue.popleft()
            rightmost = node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(rightmost)
    return result


#E[1,2,3,null,5,null,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(rightSideView(root))


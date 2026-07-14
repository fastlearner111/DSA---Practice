#Diameter of Binary Tree
root = [1,2,3,4,5]
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
    def dfs(node):
        if not node:
            return (0,0)
        
        left_diameter, left_height = dfs(node.left)
        right_diameter, right_height = dfs(node.right)

        height = 1 + max(left_height, right_height)

        diameter_through_node  = left_height + right_height
        diameter = max(left_diameter, right_diameter, diameter_through_node)

        return(diameter,height)
    return dfs(root)[0]

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(diameter(root))
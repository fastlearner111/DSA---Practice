#Kth Smallest Element in BST

#Given root of a BST and integer k, return the kth smallest value.
#
#Input:  root = [3,1,4,null,2], k = 1
#Output: 1
#
#Input:  root = [5,3,6,2,4,null,null,1], k = 3
#Output: 3

class TreeNode:
    def __init__(self, val = 0 , left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def k_smallest(root,k):
    inorder = [] 

    def dfs(node):
        if not node:
            return 
        
        dfs(node.left) # look at left value
        inorder.append(node.val) # append that left value in the inorder
        dfs(node.right) # look at the right values
    
    dfs(root) #not sure wjat this does
    return inorder[k - 1]  #same with this

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 1
print(k_smallest(root, k ))
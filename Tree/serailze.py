#Serialize and Deserialize Binary Tree
#
#Serialization is the process of converting a data structure
#or object into a sequence of bits so that it can be stored
#in a file or memory buffer, or transmitted across a network
#connection link to be reconstructed later in the same or another computer environment.
#Design an algorithm to serialize and deserialize a binary tree.
#There is no restriction on how your serialization/deserialization 
#algorithm should work. You just need to ensure that a binary tree can
#be serialized to a string and this string can be deserialized to the original tree structure.
#
#Clarification: The input/output format is the same as how LeetCode
#serializes a binary tree. You do not necessarily need to follow 
#this format, so please be creative and come up with different approaches yourself.
#
#Example 1:
#Input: root = [1,2,3,null,null,4,5]
#Output: [1,2,3,null,null,4,5]
#
#Example 2:
#Input: root = []
#Output: []


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def dfs(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        vals = []
        dfs(root)
        return ",".join(vals)
    
    def deserialize(self,data):
        def dfs():
            val = next(vals)
            if val == "null":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        
        vals = iter(data.split(","))
        dfs()

root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3, 
    TreeNode(4), TreeNode(5)))

codec =Codec()

data = codec.serialize(root)
print("Serialize:", data)


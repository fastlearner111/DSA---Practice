#Given the roots of two binary trees p and q, write a function
#to check if they are the same or not. Two binary trees are
#considered the same if they are structurally identical and
#the nodes have the same value.
#
p = [1,2,3]
q = [1,2,3]
#Output: True
#
#Input:  p = [1,2], q = [1,null,2]
#Output: False
#
#Input:  p = [1,2,1], q = [1,1,2]
#Output: False

class ListTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sametree(p,q):
    if not p  and not q:
        return True  # ==, != ,,,,,, p,q are nodes, not values, but p.value , and q.value are values so u can use != 
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return sametree(p.left, q.left) and sametree(p.right, q.right)

p = ListTree(1)
p.left = ListTree(2)
p.right = ListTree(3)

q = ListTree(1)
q.left = ListTree(2)
q.right = ListTree(3)

print(sametree(p,q))
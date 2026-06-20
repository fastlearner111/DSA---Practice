#Given two binary trees, return true if they are mirror images
#of each other (symmetric), false otherwise.

p = [1,2,3]
q = [1,3,2]
#Output: True  (mirror image)
#
#Input:  p = [1,2,3], q = [1,2,3]
#Output: False (same, not mirror)

class ListTree:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(p,q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return isMirror(p.left,q.right) and isMirror(p.right,q.left)

p = ListTree(1)
p.left = ListTree(2)
p.right  = ListTree(3)

q = ListTree(1)
q.left = ListTree(3)
q.right = ListTree(2)

print(isMirror(p,q))
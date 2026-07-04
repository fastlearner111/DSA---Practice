#Design a data structure that follows Least Recently Used cache eviction.
#
#LRUCache(capacity) → initialize with positive capacity
#get(key)           → return value if key exists, else -1
#put(key, value)    → insert or update key. If capacity reached, 
#                     evict the least recently used key.
#
#Both get and put must run in O(1) time.
#
#Input:  ["LRUCache","put","put","get","put","get","put","get","get","get"]
#        [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
#Output: [null,null,null,1,null,-1,null,-1,3,4]

class ListNode:
    def __init__(self, key = 0, val = None, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = ListNode()
        self.right = ListNode()

        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key):
        if key not in self.cache:
            return -1 
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
    
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))    # 1
cache.put(3, 3)
print(cache.get(2))    # -1
cache.put(4, 4)
print(cache.get(1))    # -1
print(cache.get(3))    # 3
print(cache.get(4))    # 4
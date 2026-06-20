#Design a HashMap without using any built-in hash table libraries.
#
#Implement the MyHashMap class:
#- put(key, value): inserts key-value pair, updates value if key exists
#- get(key): returns value if key exists, -1 if not
#- remove(key): removes key and its value if key exists
#
#Input:
#["MyHashMap","put","put","get","get","put","get","remove","get"]
#[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]
#Output: [null,null,null,1,-1,null,1,null,-1]

#- contains(key): returns True if key exists, False if not
#
#Input:  put(1,1), contains(1), contains(2)
#Output: True, False

class MyHashMap:

    def __init__(self):
        self.data = {}
    
    def put(self,key, value):
        self.data[key] = value
        
    def get(self,key):
        if key in self.data:
            return self.data[key] 
        return -1

    def remove(self,key):
        if key in self.data:
         del self.data[key]

    def contains(self,key):
        if key in self.data:
            return True
        return False
            
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
obj.put(1,1)

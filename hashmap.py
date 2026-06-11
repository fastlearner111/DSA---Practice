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
            
obj = MyHashMap()
obj.put(1,1)
obj.put(2,2)
print(obj.get(1))
print(obj.get(3))
obj.put(2,1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))

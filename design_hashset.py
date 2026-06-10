#Design a HashSet without using any built-in hash table libraries.
#
#Implement the MyHashSet class:
#- add(key): inserts key into the HashSet
#- remove(key): removes key from the HashSet
#- contains(key): returns True if key exists, False otherwise
#
#Input:
#["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
#[[],[1],[2],[1],[3],[2],[2],[2],[2]]
#Output: [null,null,null,True,False,null,True,null,False]


class MyHashSet:
    def __init__(self):
        self.data = set()
    def add(self,x):
        self.data.add(x)
    def remove(self,x):
        self.data.remove(x)
    def contains(self,x):
            return x in self.data

obj = MyHashSet()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))


        


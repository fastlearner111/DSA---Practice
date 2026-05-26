#Given an array, return True only if any number appears
#MORE THAN TWICE. Appearing exactly twice does not count.
s =  [1, 2, 3, 1, 1]
#Output: True  (1 appears 3 times)

#Input: [1, 2, 3, 1]
#Output: False  (1 appears exactly twice, not more)

# first seen is gonna hold empty dict seen = {}
# count = 0
# for loop
# if number in s
# count[number] +=1
# else count[number] = 1
# count[number] > 2 then return True 
# else False

def repeating_count(s):
    count = {}

    for number in s:
        if number in count:
            count[number] +=1
        else:
            count[number] = 1
    for value in count.values():
     if value > 2:
        return True
    return False
print(repeating_count(s))
    
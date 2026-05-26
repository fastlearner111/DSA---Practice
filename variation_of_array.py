#Given two arrays, return True if they share any common element.
s = [1, 2, 3], [4, 5, 3]
#Output: True

#Input: [1, 2, 3], [4, 5, 6]
#Output: False

s1 = [1,2,7]
s2 = [4,5,3]

def share_element(s1,s2):
    seen = set(s1)

    for number in s2:
     if number in seen:
      return True

    return False 
print(share_element(s1,s2))

    
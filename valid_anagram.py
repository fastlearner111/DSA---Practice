s1 = "anagram"
s2 = "nagaram"

# For this we are gonna need two variable one is gonna be nums1, and the other nums2
# then we are gonna use two loops, one for nums1 and other for nums2, then lopp foreach if char in seen then +1
# else 1, then same for s2, 
# then after that we check is counts1 and 2 are equal,
# if yes then true 
# else false
def check_anagram(s1,s2):
  counts1 ={}
  counts2 ={}
  
  for char in s1:
   if char in counts1:
    counts1[char] +=1
   else:
    counts1[char] = 1
 
  for char in s2:
   if char in counts2:
    counts2[char] += 1
   else:
    counts2[char] =1

  if counts1 == counts2:
   return True
 
  return False

print(check_anagram(s1,s2))
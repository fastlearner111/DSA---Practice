#Write a function that reverses a string.
#The input is given as an array of characters.
#Modify the array in-place with O(1) extra memory.
#
s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#
#Input:  s = ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]

#Pattern - Two Pointer
# Dict = two pointer
# approach - we need to reverse the left side and then reversre the right side and set it equal
# then move the pointer and then return it
# Big O - On, O1

def reverse_string(s):
    left = 0
    right = len(s) - 1

    while left < right:
        s[left], s[right] = s[right], s[left]

        left += 1
        right -= 1

reverse_string(s)
print(s)
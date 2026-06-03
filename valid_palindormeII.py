#Given a string s, return true if it can be a palindrome 
#after deleting at most one character.

#s = "aba"
#Output: True

#s = "abca"
#Output: True  (delete 'c' or 'b')

s = "abc"
#Output: False

#  first this is  two pointer 
# the variable needed are left and right , this are the two pointer
# steps: we use while loop , inside that we are gonna check if the left is equal to right or niot 
# if not then return false
# else we move the pointer inward,

def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):

    left = 0
    right = len(s) - 1

    while left < right: 
        if s[left] != s[right]:
            skip_left = is_palindrome(s,left + 1, right)
            skip_right = is_palindrome(s,left, right-1)
            return skip_left or skip_right
    
        left += 1
        right -= 1
    return True
print(valid_palindrome(s))

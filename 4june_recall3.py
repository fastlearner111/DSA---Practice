#Given a string s, return true if it can be a palindrome 
#after deleting at most one character.

s = "raceacar"
#Output: True

#Input:  s = "abcdef"
#Output: False

def is_palindrome(s,left,right):
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
    
def check_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]: 
          skip_left = is_palindrome(s, left + 1, right)
          skip_right = is_palindrome(s,left,right - 1 )
          return skip_left or skip_right
       
        left += 1
        right -= 1

    return True
print(check_palindrome(s))
    

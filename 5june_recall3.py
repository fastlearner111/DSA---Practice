#Given a string, determine if it is a palindrome considering
#only alphanumeric characters and ignoring case.
#
s = "A man, a plan, a canal: Panama"
#Output: True
#
#s = "race a car"
#Output: False
#
#Input:  s = " "
#Output: True

#pattern - two pointers
# variable = left and right and one cleaned to make everything lowercase and see if isalnum or not
# pattern, : use while loop
            # then check if left = right
            # if not then return False
            # else move the pointer inward
            # then return 
            # then print

def check_palindrome(s):
    
    cleaned = [c.lower() for c in s if c.isalnum()]
    left = 0
    right = len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True
print(check_palindrome(s))

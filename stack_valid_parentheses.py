#Given a string s containing just '(', ')', '{', '}', '[' and ']', 
#return true if the input string is valid.

s = "()"
#Output: True

#Input:  s = "()[]{}"
#Output: True

#Input:  s = "(]"
#Output: False

#Input:  s = "([)]"
#Output: False

def check_parenthses(s):
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in s:
        if char in mapping:   
            if not stack or stack[-1] != mapping[char]:
              return False
            stack.pop()
        else:
            stack.append(char)
            return True
    return []
print(check_parenthses(s))
#Given a string containing just '(', ')', '{', '}', '[', ']',
#return True if the string is valid.
#
#Valid means:
#- Open brackets closed by same type
#- Closed in correct order
#
s = "()"
#Output: True
#
#Input:  s = "()[]{}"
#Output: True
#
#Input:  s = "(]"
#Output: False
#
#Input:  s = "([)]"
#Output: False

# Pattern - Stack
# Approach - use a dict to map closing→opening brackets. Push opening to stack. 
#            When closing found — check if top of stack matches. Pop if yes, False if no.
# Data Structure - stack (list) + hashmap (dict)
# Big O - O(n) time, O(n) space

def valid_parenthesis(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
print(valid_parenthesis(s))
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
#determine if the input string is valid.
#
#A string is valid if:
#- Every open bracket is closed by the same type of bracket
#- Open brackets are closed in the correct order
#- Every close bracket has a corresponding open bracket

s = "()[]{}"
#Output: True
#
#Input:  s = "([)]"
#Output: False
#
#Input:  s = "{[]}"
#Output: True

def check_parentheses(s):
    stack = []
    mapping = {")": "(", "]": "[", "}":"{"}

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
        
    return not stack
print(check_parentheses(s))
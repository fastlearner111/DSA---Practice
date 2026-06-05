#Given a string s of just brackets, return true if valid.

s = "{[()]}"
#Output: True

#Input:  s = "{[(])}"  
#Output: False

def check_parentheses(s):

    stack = []
    mapping = {")": "(" , "]": "[" , "}": "{"}

    for char in s:
        if char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            stack.append(char)
    return not stack
print(check_parentheses(s))

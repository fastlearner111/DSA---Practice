#Evaluate arithmetic expression in Reverse Polish Notation.
#Operators: +, -, *, /  Division truncates toward zero.
#
tokens = ["2","1","+","3","*"]
#Output: 9
#
#Input:  tokens = ["4","13","5","/","+"]
#Output: 6

def polish(tokens):
    stack = []

    for token in tokens:
        if token not in ["+", "-", "*", "/"]:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()

            if token == "+":
                stack.append(left + right)
            elif token == "-":
                stack.append(left - right)
            elif token == "*":
                stack.append(left * right)
            elif token == "/":
                stack.append(int(left / right))
    return stack[-1]
print(polish(tokens))
        
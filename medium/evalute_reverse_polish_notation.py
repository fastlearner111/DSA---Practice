#Evaluate an arithmetic expression in Reverse Polish Notation.
#
#Valid operators: +, -, *, /
#Each operand is an integer or another expression.
#Division truncates toward zero.
#
tokens = ["2","1","+","3","*"]
#Output: 9   ((2+1)*3 = 9)
#
#Input:  tokens = ["4","13","5","/","+"]
#Output: 6   (4+(13/5) = 6)
#
#Input:  tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
#Output: 22

# Pattern - Stack
# Approach - Not sure
# data strcut = 
# Big O = On, On

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




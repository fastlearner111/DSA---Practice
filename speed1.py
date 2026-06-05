#Given a list of operations, return the sum of all scores.
ops = ["3","4","C","D","+","D"]
#Output: ?

def check_sum(ops):
    stack = []

    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "D":
            stack.append(stack[-1] * 2)
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
    return sum(stack)
print(check_sum(ops))
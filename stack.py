#You are given a list of strings operations where each 
#operation is one of the following:

#- An integer x: Record a new score of x
#- "+": Record a new score that is the sum of the previous two scores
#- "D": Record a new score that is double the previous score
#- "C": Invalidate the previous score, removing it from the record

#Return the sum of all scores on the record.

ops = ["5","2","C","D","+"]
#Output: 30

#Input:  ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27

def return_sum(ops):
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
print(return_sum(ops))

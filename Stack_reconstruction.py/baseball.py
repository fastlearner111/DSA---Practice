#You are keeping score for a baseball game. The record is a list of strings.
#Each string can be:
#- An integer: record a new score of that integer
#- "+": record a new score that is the sum of the previous two scores
#- "D": record a new score that is double the previous score
#- "C": invalidate the previous score, removing it from the record
#
#Return the sum of all scores.
#
ops = ["5","2","C","D","+"]
#Output: 30
#
#Input:  ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27
#
#Input:  ops = ["1","C"]
#Output: 0

# Pattern - Stack
# Approach - we need 4 condition to check, 
# 1) IF op == "+" then the sum
# 2) if op == "D" then double
# 3) if op ==  "C" then remove
# 4) if int then change the strinf to int then return it
# Data Structure = Stack
# Big O - On, On

def keep_record(ops):
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
print(keep_record(ops))

#You are keeping score for a baseball game with unusual rules.
#You are given a list of strings called operations.
#
#At each step:
#- An integer x: record a new score of x
#- '+': record a sum of the previous two scores
#- 'D': record double the previous score
#- 'C': invalidate (remove) the previous score

#Return the sum of all scores on the record.

#ops = ["5","2","C","D","+"]
#Output: 30

ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27

#pattern : stack, variable: stack = [], steps,
#we first need to use loop for this,
#and we need four conditions, one for + thats return stack 1 + stack2,
#second for "C" that pops the last entry, "D" for stack[-1] * 2,and in the else part we put if there is number 
#then we appedn it and the return stack and print

def check_sum(ops):
    stack = []

    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
        elif op == "C":
            stack.pop()
        elif op == "D":
            stack.append(stack[-1] * 2)
        else:
            stack.append(int(op))
    return sum(stack)
print(check_sum(ops))

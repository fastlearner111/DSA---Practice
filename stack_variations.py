#Given a list of operations, return the maximum score 
#recorded at any point during the game, not the final sum.

ops = ["5","2","C","D","+"]
#Output: 15  (maximum single score recorded was 15)

##Input:  ops = ["5","-2","4","C","D","9","+","+"]
#Output: 27  (maximum single score recorded was 27... 
#wait let me verify)

def check_max(ops):
    stack = []
    max_score = 0

    for op in ops:
        if op == "+":
            stack.append(stack[-1] + stack[-2])
            max_score = max(max_score,stack[-1])
        elif op == "D":
            stack.append(stack[-1] * 2)
            max_score = max(max_score,stack[-1])
        elif op == "C":
            stack.pop()
        else:
            stack.append(int(op))
            max_score = max(max_score,stack[-1])
    return max_score
print(check_max(ops))
        
            

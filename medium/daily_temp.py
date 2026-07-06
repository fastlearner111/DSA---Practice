#Given array of daily temperatures, return array where each element 
#is the number of days until a warmer temperature.
#If no warmer day exists, put 0.
#
temperatures = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]
#
#Input:  temperatures = [30,40,50,60]
#Output: [1,1,1,0]
#
#Input:  temperatures = [30,60,90]
#Output: [1,1,0]

def temp(temperatures):
    stack = []
    result = [0] * len(temperatures) # this one cretes a 0s of length temp, the reason is 
    # it will be easy for us to sort

    for i in range(len(temperatures)): # loops every index in temperatures
        while stack and temperatures[i] > temperatures[stack[-1]]: # if not in stack and if the current day temp greater than the top of stack
            idx = stack.pop() # then pop not sure , i think the top one in the stack
            result[idx] = i - idx # count the days for the next warmer days
        stack.append(i) # not sure
    return result
print(temp(temperatures))
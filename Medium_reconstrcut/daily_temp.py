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
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            idx = stack.pop()
            result[idx] = i - idx
        stack.append(i)
    return result
print(temp(temperatures))
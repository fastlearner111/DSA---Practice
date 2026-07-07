#Given temperatures array, return days until warmer temperature.
#
temperature = [73,74,75,71,69,72,76,73]
#Output: [1,1,4,2,1,1,0,0]

def daily_temp(temperature):
    stack = []
    result = [0] * len(temperature)


    for i in range(len(temperature)):
        while stack and temperature[i] > temperature[stack[-1]]:
            idx = stack.pop()
            result[idx] = i -idx 
        stack.append(i)
    return result
print(daily_temp(temperature))
#n cars going to target. Find number of car fleets.
#
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
#Output: 3

# Pattern - Stack
# Approach - 
# Data Structure - 
# Big O -On, On

def car_fleet(target, position, speed):
    stack = []
    pair = sorted(zip(position, speed), reverse= True)

    for pos, spd in pair:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)
print(car_fleet(target, position,speed))
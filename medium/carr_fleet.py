#There are n cars going to the same destination. You are given:
#- position: array of car positions
#- speed: array of car speeds
#- target: the destination
#
#A car fleet is a group of cars that arrive at the destination together.
#A faster car that catches up to a slower car becomes part of its fleet.
#
#Return the number of car fleets that arrive at the destination.
#
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
#Output: 3
#
#Input:  target = 10, position = [3], speed = [3]
#Output: 1
#
#Input:  target = 100, position = [0,2,4], speed = [4,2,1]
#Output: 1


def carfleet(postion, speed, target):
    pairs = sorted(zip(position, speed), reverse = True)
    stack = []

    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)
    return len(stack)
print(carfleet(position, speed, target))
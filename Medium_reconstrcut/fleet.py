#n cars going to target. Find number of car fleets.
#
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
#Output: 3

def carfleet(target, position, speed):
    pairs = sorted(zip(position, speed), reverse = True)
    stack = []

    for pos, spd in pairs:
      time = (target - pos) / spd
      if not stack or time > stack[-1]:
         stack.append(time)
    return len(stack)
print(carfleet(target, position, speed))

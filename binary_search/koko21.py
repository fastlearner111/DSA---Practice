piles = [1,4,3,2]
h = 9

#Output: 2

def iseating(piles,h):

    def canFinish(speed):
        total_hours_needed = 0
        for pile in piles:
            total_hours_needed += (pile + speed - 1) // speed
        return total_hours_needed <= h

    left = 1
    right = max(piles)
    best = right

    while left <= right:
        mid = (left + right) // 2

        if canFinish(mid):
            best = mid
            right = mid - 1

        else:
            left = mid + 1

    return best
print(iseating(piles,h))
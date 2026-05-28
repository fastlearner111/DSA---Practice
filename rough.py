nums = [1,4,1,2]


def conc_check(nums):
    ans = []

    for n in range(3):
       ans += nums
    return ans
print(conc_check(nums))

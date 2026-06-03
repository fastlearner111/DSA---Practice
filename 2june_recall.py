#Given two integer arrays nums1 and nums2, sorted in 
#non-decreasing order, and integers m and n, merge 
#nums2 into nums1 in-place.

nums1 = [2,4,6,0,0,0]
m = 3
nums2 = [1,3,5]
n = 3
#Output: [1,2,3,4,5,6]

def sorted_merge(nums1, m, nums2, n):

    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p3]= nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -=1
        p3 -= 1

    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -=1
        p3 -= 1

    return nums1
print(sorted_merge(nums1,m,nums2,n))
            
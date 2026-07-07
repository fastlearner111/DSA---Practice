#You are given two sorted integer arrays nums1 and nums2.
#Merge nums2 into nums1 in-place. nums1 has enough space at the end.
#
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#Output: [1,2,2,3,5,6]
#
#Input:  nums1 = [1], m = 1, nums2 = [], n = 0
#Output: [1]
#
#Input:  nums1 = [0], m = 0, nums2 = [1], n = 1
#Output: [1]

# Pattern - Two Pointer
# Data struct - Two pointer, or maybe 3 pointer
# approach - 
# big O - On, O1

def merge_sorted(nums1, nums2):
    p1 = m - 1
    p2 = n -1
    p3 = m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1
    while p2 >= 0:
        nums1[p3] = nums2[p2]
        p2 -= 1
        p3 -= 1
    return nums1
print(merge_sorted(nums1,nums2))
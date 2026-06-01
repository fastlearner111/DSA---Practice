#You are given two integer arrays nums1 and nums2, sorted 
##in non-decreasing order, and two integers m and n, 
#representing the number of elements in nums1 and nums2.

#Merge nums2 into nums1 as one sorted array in-place.

#nums1 has extra zeros at the end to hold nums2 elements.

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
#Output: nums1 = [1,2,2,3,5,6]

def merge_sort(nums1,nums2):
    p1 = m-1
    p2 = n-1
    p3 = m+n-1

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
print(merge_sort(nums1,nums2))

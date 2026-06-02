#You are given two integer arrays nums1 and nums2, sorted 
#in non-decreasing order, and two integers m and n.
#Merge nums2 into nums1 as one sorted array in-place.
#nums1 has extra zeros at the end.

nums1 = [1,3,5,0,0,0]
m = 3
nums2 = [2,4,6]
n = 3
#Output: [1,2,3,4,5,6]

# we need three pointers for this, so the pattern is three pointers
#p1,p2,p3 name of the pointer
# then we are gonna use a while loop
# inside while we are gonna comapare the last valur

def merge_sorted(nums1,m,nums2,n):
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
print(merge_sorted(nums1,m,nums2,n))
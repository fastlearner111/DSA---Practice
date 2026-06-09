#You are a product manager and currently leading a team to develop
#a new product. Since each version is developed based on the previous
#version, all the versions after a bad version are also bad.
#
#You are given an API bool isBadVersion(version) which returns whether
#a version is bad. Find the first bad version.

n = 5
bad = 4
#Output: 4
##
##Input:  n = 1, bad = 1
#Output: 1

def isBadVersion(version):
    return version >= bad


def firstBadVersion(n):
    left = 1
    right = n
    result = n

    while left <= right:
        mid = (left + right ) // 2
        if isBadVersion(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return right
print(firstBadVersion(n))
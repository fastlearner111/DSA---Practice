#You are a product manager. All versions after a bad version
#are also bad. Given API isBadVersion(version), find the
#first bad version.

n = 5
bad = 4
#Output: 4

def bad_version(version):
    return version >= bad

def isbad_version(n, bad):
    left  = 1
    right = n

    while left <= right:
        mid = (left + right) // 2
        if bad_version(mid):
            result = mid 
            right = mid - 1
        else:
            left = mid + 1
    return result
print(isbad_version(n,bad))
    
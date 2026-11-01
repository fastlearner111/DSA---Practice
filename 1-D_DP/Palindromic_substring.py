s = "abc"
#Output: 3


class Solution:
    def countSubstring(self):
        count = 0

        def expand(left, right):
            local_count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                local_count += 1
                left += 1
                right -= 1
            return local_count

        for i in range(len(s)):
            count += expand(i, i)
            count += expand(i, i + 1)

        return count

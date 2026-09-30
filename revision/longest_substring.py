s = "zxyzxyz"
#Output: 3

class Solution:
    def longest_sub(self, s):
        left = 0
        max_len = ()
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

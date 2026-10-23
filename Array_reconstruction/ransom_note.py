ransomNote = "a"
magazine = "b"
Output: False

#Input: ransomNote = "aa", magazine = "ab"
#Output: False

from collections import Counter
class Solution:
    def ransom(self, ransomNote, magazine):
        note_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        for char, count in note_count.items():
            if mag_count[char] < count:
                return False
        return True
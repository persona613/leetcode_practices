'''
Runtime: 63 ms, faster than 83.61% of Python3 online submissions for Ransom Note.
Memory Usage: 14.1 MB, less than 93.85% of Python3 online submissions for Ransom Note.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_set = set(ransomNote)
        mag_set = set(magazine)
        if not ran_set <= mag_set:
            return False
        inter_set = ran_set & mag_set
        for s in inter_set:
            count_ran = ransomNote.count(s)
            count_mag = magazine.count(s)
            if count_ran > count_mag:
                return False
        return True
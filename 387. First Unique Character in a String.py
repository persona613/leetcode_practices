'''
Runtime: 69 ms, faster than 94.35% of Python3 online submissions 
Memory Usage: 16.83 MB, less than 59.20% of Python3 online submissions
'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                if s.count(s[i]) == 1:
                    return i
                seen.add(s[i])
        return -1
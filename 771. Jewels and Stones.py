'''
Runtime: 42 ms, faster than 79.53% of Python3 online submissions 
Memory Usage: 13.9 MB, less than 59.97% of Python3 online submissions
'''

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for s in stones:
            if s in jewels:
                ans += 1
        return ans
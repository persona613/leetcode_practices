'''
Runtime: 2190 ms, faster than 5.58% of Python3 online submissions 
Memory Usage: 14.0 MB, less than 50.82% of Python3 online submissions
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        count = 0
        bag = set()
        i = 0
        j = 0
        while j < len(s):
            if s[j] in bag:
                ans.add(count)
                count = 0
                bag.clear()
                i += 1
                j = i
            else:
                bag.add(s[j])
                count += 1
                j += 1
        
        ans.add(count)
        return max(ans)   
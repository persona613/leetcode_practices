"""
569 ms runtime beats 99.26%
22.27 MB memory beats 33.26%
"""
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d = {0: -1}
        curr = ans = 0
        for i in range(len(nums)):
            curr += 1 if nums[i]==1 else -1
            try:
                diff = i - d[curr]
                if diff > ans:
                    ans = diff
            except:
                d[curr] = i
        return ans
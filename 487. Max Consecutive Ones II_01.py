"""
300 ms runtime beats 92.23%
16.52 MB memory beats 44.54%
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # zi = zero index
        zi = -1
        # curr 1s count
        cnt = ans = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if cnt > ans:
                    ans = cnt
                cnt = i - zi
                zi = i
            else:
                cnt += 1
        return max(ans, cnt)
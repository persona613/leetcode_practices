"""
1391 ms runtime beats 26.84%
35.49 MB memory beats 11.78%
"""
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ps = [nums[0]]
        for v in nums[1:]:
            ps.append(v + ps[-1])
        res = []
        n = len(nums)
        d = k * 2 + 1
        for i in range(n):
            if i - k < 0 or i + k >= n:
                res.append(-1)
            else:
                a = ps[i+k] - ps[i-k] + nums[i-k]
                res.append(a // d)
        return res
"""
3 ms runtime beats 87.77%
16.79 MB memory beats 55.71%
"""
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1 or k == 1: return nums
        ln = 1
        res = []
        for i in range(1, k):
            if nums[i] - nums[i - 1] == 1:
                ln += 1
            else:
                ln = 1
        if ln == k:
            res.append(nums[i])
        else:
            res.append(-1)

        for i in range(k, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                ln += 1
                if ln >= k:
                    res.append(nums[i])
                else:
                    res.append(-1)
            else:
                ln = 1
                res.append(-1)
        return res
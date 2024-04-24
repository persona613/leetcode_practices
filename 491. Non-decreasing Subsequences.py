"""
142 ms runtime beats 64.20%
24.95 MB memory beats 34.48%
"""
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(i, path):
            if i == n and len(path) >= 2:
                res.add(tuple(path))
                return

            if len(path) >= 2:
                res.add(tuple(path))
            for j in range(i, n):
                # prune duplicate branch
                if j > i and nums[j] == nums[j - 1]:
                    continue
                if not valid[nums[j]]:
                    continue
                if not path or path[-1] <= nums[j]:
                    path.append(nums[j])
                    backtrack(j + 1, path)
                    path.pop()

        valid = dict.fromkeys(nums, True)
        n = len(nums)
        res = set()
        backtrack(0, [])
        return res
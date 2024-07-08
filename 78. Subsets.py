"""
38 ms runtime beats 50.35%
16.95 MB memory beats 8.15%
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        def dfs(i, path):
            nonlocal n
            if i == n:
                res.append(path[:])
                return

            # take curr element
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
            # not take curr
            dfs(i + 1, path)

        res = []
        n = len(nums)
        dfs(0, [])
        return res

"""
17285 ms runtime beats 5%
31.4 MB memory beats 5.9%
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        t = len(nums)-1
        # double defaultdict {i//1000: {i: int)}} 
        # memo = defaultdict(lambda: defaultdict(int))
        memo = defaultdict(dict)
        def dfs(pos):
            if pos in memo[pos//1000]:
                return memo[pos//1000][pos]
            if pos == 0:
                memo[0][0] = 0
                return 0
            path = float('inf')
            for i in range(1, 1001):
                if pos-i < 0:
                    break
                if nums[pos-i] >= i:
                    path = min(path, dfs(pos-i))
            memo[pos//1000][pos] = path+1
            return path+1
        return dfs(t)

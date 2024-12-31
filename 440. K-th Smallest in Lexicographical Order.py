"""
32 ms runtime beats 81.09%
16.76 MB memory beats 30.85%
"""
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:

        # curr-node(include) subtree's count
        @lru_cache(None)
        def count(curr, n):
            cnt = 1
            p = 1
            low = curr * (10 ** p)
            high = low + (10 ** p) - 1
            while high <= n:
                cnt += high - low + 1
                p += 1
                low *= 10
                high = low + (10 ** p) - 1
            if low <= n:
                cnt += n - low + 1
            return cnt
        
        # curr-node, target i-th element
        def dfs(curr, t, n):
            if t == 1:
                return curr
            
            curr_cnt = count(curr, n)
            # target in curr-subtree
            if t <= curr_cnt:
                return dfs(curr * 10, t - 1, n)
            # target in next subtree
            else:
                return dfs(curr + 1, t - curr_cnt, n)

        return dfs(1, k, n)
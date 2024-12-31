"""
62 ms runtime beats 91.89%
33.86 MB memory beats 48.00%
"""
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        pool = set(nums)
        ans = -1
        while pool:
            curr = pool.pop()
            cnt = 1

            # root of curr
            rt = curr ** 0.5
            while rt in pool:
                pool.remove(rt)
                cnt += 1
                rt **= 0.5

            # square of curr
            sq = curr ** 2
            while sq in pool:
                pool.remove(sq)
                cnt += 1
                sq **= 2

            if cnt > 1:
                ans = max(ans, cnt)
        return ans
"""
64 ms runtime beats 96.25%
18.71 MB memory beats 61.05%
"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mi = min(cnt.keys())        
        mx = max(cnt.keys())
        for key in range(mi, mx + 1):
            # not take curr
            pre = cnt.get(key - 1, 0)
            # take=curr + prepre, if curr not exist, bridge it
            take = key * cnt.get(key, 0) + cnt.get(key - 2, 0)
            cnt[key] = max(pre, take)

        return cnt[mx]
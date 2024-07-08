"""
397 ms runtime beats 5.25%
21.44 MB memory beats 55.53%
"""
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # pre sum
        ps = [nums[0] % k]
        for v in nums[1:]:
            ps.append((ps[-1]+ v) % k)
        
        cnt = defaultdict(int)
        cnt[0] = 1
        ans = 0
        for r in ps:
            ans += cnt[r]
            cnt[r] += 1
        return ans
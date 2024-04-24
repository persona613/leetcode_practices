"""
48 ms runtime beats 23.13%
16.56 MB memory beats 93.22%
"""
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def sep(threshold):
            p = 0
            sm = 0
            mx = -inf
            for v in nums:
                if sm + v > threshold:
                    p += 1
                    mx = max(mx, sm)
                    sm = v
                else:
                    sm += v
            return p + 1, max(mx, sm)

        l = min(nums)
        r = sum(nums)
        while l < r:
            mid = (l + r) // 2
            p, max_party = sep(mid)
            # print(f"l={l},r={r},mid={mid}, p={p}, maxp={max_party}")
            if p > k:
                l = mid + 1
            else:
                r = mid
        
        p, ans = sep(r)
        # print(l, p, ans)
        return ans
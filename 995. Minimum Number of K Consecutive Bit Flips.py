"""
1590 ms runtime beats 5.63%
19.50 MB memory beats 76.06%
"""
class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        mask = 1 << (k - 1)
        q = nums[0]
        for i in range(1, k):
            q <<= 1
            q |= nums[i]

        ans = 0
        flip = (1 << k) - 1
        for i in range(k, len(nums)):
            if q & mask == 0:
                q ^= flip
                ans += 1

            # close left-most and add new bit
            q ^= mask
            q <<= 1
            q |= nums[i]
        
        z = q.bit_count()
        if z == k:
            return ans
        elif z == 0:
            return ans + 1
        return -1
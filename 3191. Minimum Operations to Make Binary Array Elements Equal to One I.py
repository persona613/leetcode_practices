"""
998 ms runtime beats 50%
20.36 MB memory beats 50%
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        mask = 1 << 2
        q = nums[0]
        for i in range(1, 3):
            q <<= 1
            q |= nums[i]

        ans = 0
        # 111
        flip = (1 << 3) - 1
        for i in range(3, len(nums)):
            # check q[0] is 0
            if q & mask == 0:
                # filp q
                q ^= flip
                ans += 1

            # close left most bit
            q ^= mask
            # append new val
            q <<= 1
            q |= nums[i]

        b = q.bit_count()
        if b == 3:
            return ans
        elif b == 0:
            return ans + 1
        return -1
"""
1588 ms runtime beats 67.44%
35.76 MB memory beats 72.93%
"""
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:

        def operate(num, vector):
            p = 0
            while num > 0:
                if num & 1:
                    bcnt[p] += 1 * vector
                num >>= 1
                p += 1
            return convert(bcnt)

        def convert(bcnt):
            ret = 0
            mask = 1
            for i in range(len(bcnt)):
                if bcnt[i] > 0:
                    ret += mask
                mask <<= 1
            return ret

        if max(nums) >= k:
            return 1
        # bit frequency array
        bcnt = [0] * 32
        left = 0
        n = len(nums)
        ans = float("inf")
        for right in range(n):
            # add num
            currOR = operate(nums[right], 1)
            while currOR >= k:
                ans = min(ans, right - left + 1)
                # remove num
                currOR = operate(nums[left], -1)
                left += 1
        return -1 if ans == float("inf") else ans
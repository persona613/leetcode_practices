"""
15 ms runtime beats 93.02%
17.01 MB memory beats 6.27%
"""
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # modify intelligently build LIS
        LIS = [0] * n
        LIS[0] = 1
        iq = [nums[0]]
        for i in range(1, n):
            if nums[i] > iq[-1]:
                iq.append(nums[i])
                LIS[i] = len(iq)
            else:
                t = bisect.bisect_left(iq, nums[i])
                # replace minor element to open more possibility
                iq[t] = nums[i]
                # record LIS length end at i
                LIS[i] = t + 1

        # LDS: LIS from right
        LDS = [0] * n
        LDS[-1] = 1
        iq = [nums[-1]]
        for i in range(n - 2, -1, -1):
            if nums[i] > iq[-1]:
                iq.append(nums[i])
                LDS[i] = len(iq)
            else:
                t = bisect.bisect_left(iq, nums[i])
                iq[t] = nums[i]
                LDS[i] = t + 1

        mxln = 0
        for i in range(n):
            if LIS[i] == 1 or LDS[i] == 1:
                continue
            mxln = max(mxln, LIS[i] + LDS[i] - 1)
        return n - mxln
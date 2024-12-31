"""
28 ms runtime beats 59.17%
20.54 MB memory beats 47.78%
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # window sum
        wsum = sum(nums[:k])
        arr = [wsum]
        for i in range(k, len(nums)):
            wsum += nums[i] - nums[i - k]
            arr.append(wsum)

        ln = len(arr)
        # prefix max_val and lexic index
        preval = [0] * ln
        preidx = [0] * ln
        preval[0] = arr[0]
        for i in range(1, ln):
            if arr[i] > preval[i - 1]:
                preval[i] = arr[i]
                preidx[i] = i
            else:
                preval[i] = preval[i - 1]
                preidx[i] = preidx[i - 1]

        # suffix max_val and lexic index
        sufval = [0] * ln
        sufidx = [0] * ln
        sufval[ln - 1] = arr[ln - 1]
        sufidx[ln - 1] = ln - 1
        for i in range(ln - 2, -1, -1):
            if arr[i] >= sufval[i + 1]:
                sufval[i] = arr[i]
                sufidx[i] = i
            else:
                sufval[i] = sufval[i + 1]
                sufidx[i] = sufidx[i + 1]

        mxsum = 0
        res = []
        for i in range(k, ln - k):
            curr_sum = arr[i] + preval[i - k] + sufval[i + k]
            if curr_sum > mxsum:
                mxsum = curr_sum
                res = [preidx[i - k], i, sufidx[i + k]]
        return res
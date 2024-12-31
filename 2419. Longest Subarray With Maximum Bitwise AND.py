"""
661 ms runtime beats 48.00%
30.84 MB memory beats 85.09%
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mxln = 0
        mxval = 0
        ln = 0
        for v in nums:
            if v > mxval:
                mxval = v
                ln = 1
                mxln = 1
            elif v == mxval:
                ln += 1
                mxln = max(mxln, ln)
            else:
                ln = 0
        return mxln
"""
464 ms runtime beats 87.95%
27.21 MB memory beats 21.60%
"""
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mxq = deque()
        miq = deque()
        ans = l = 0
        for r in range(len(nums)):

            while mxq and nums[mxq[-1]] < nums[r]:
                mxq.pop()
            while miq and nums[miq[-1]] > nums[r]:
                miq.pop()

            mxq.append(r)
            miq.append(r)

            while nums[mxq[0]] - nums[miq[0]] > limit:
                if mxq[0] == l:
                    mxq.popleft()
                if miq[0] == l:
                    miq.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
"""
1124 ms runtime beats 93.50%
33.31 MB memory beats 27.27%
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(len(nums)):            
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if q[0] + k == i:
                q.popleft()

            if i >= k - 1:
                res.append(nums[q[0]])
        return res
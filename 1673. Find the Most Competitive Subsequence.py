"""
873 ms runtime beats 92.68%
29.38 MB memory beats 88.72%
"""
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        n = len(nums)
        p = k
        res = []
        for i in range(n):
            if p > n - i:
                res.append(nums[q.popleft()])
            while q and nums[q[-1]] > nums[i]:
                q.pop()
            q.append(i)
        res.append(nums[q[0]])
        return res
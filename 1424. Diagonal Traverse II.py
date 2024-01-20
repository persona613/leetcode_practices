"""
780 ms runtime beats 73.29%
37.03 MB memory beats 85.73%
"""
class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = deque([(0,0)])
        n = len(nums)
        while q:
            i, j = q.popleft()
            res.append(nums[i][j])
            if j == 0 and i+1<n:
                q.append((i+1, j))
            if j+1<len(nums[i]):
                q.append((i, j+1))
        return res
        
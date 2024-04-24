"""
775 ms runtime beats 38.78%
31.72 MB memory beats 69.21%
"""
class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res = [0] * n
        q = deque()
        for i in range(n-1, -1, -1):
            while q and heights[q[-1]] < heights[i]:
                j = q.pop()
                if q:
                    res[j] += 1 # look right
                res[i] += 1 # look left
            q.append(i)
        while q:
            j = q.pop()
            if q:
                res[j] += 1
        return res
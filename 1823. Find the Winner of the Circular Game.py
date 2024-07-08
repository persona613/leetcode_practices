"""
127 ms runtime beats 24.58%
16.56 MB memory beats 49.47%
"""
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([i for i in range(1, n + 1)])
        while len(q) > 1:
            # turn k-1 times
            for _ in range(k - 1):
                q.append(q.popleft())
            q.popleft()
        return q.popleft()
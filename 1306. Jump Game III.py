"""
215 ms runtime beats 94.27%
23.50 MB memory beats 75.30%
"""
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        seen = {start}
        q = deque([start])
        dirs = [1, -1]
        while q:
            curr = q.popleft()
            a = arr[curr]
            if a == 0:
                return True
            for d in dirs:
                ni = curr + d * a
                if 0 <= ni < n and ni not in seen:
                    seen.add(ni)
                    q.append(ni)
        return False
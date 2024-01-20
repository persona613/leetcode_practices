"""
38 ms runtime beats 99.02%
17.42 MB memory beats 35.78%
"""
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque(senate)
        w = deque()
        while len(q) > 1:
            if not w:
                w.append(q.popleft())
            while w and q:
                if w[0] != q[0]:
                    q.popleft()
                    q.append(w.popleft())
                else:
                    w.append(q.popleft())
            if not q:
                q.extend(w)
                break

        return "Radiant" if q[0] == "R" else "Dire"
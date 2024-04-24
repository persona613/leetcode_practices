"""
52 ms runtime beats 31.10%
16.61 MB memory beats 16.09%
"""
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        for i, t in enumerate(tickets):
            q.append([i, t])
        cnt = tickets[k]
        tm = 0
        while cnt:
            i, t = q.popleft()
            tm += 1
            if i == k:
                cnt -= 1
            if t > 1:
                q.append([i, t-1])
        return tm
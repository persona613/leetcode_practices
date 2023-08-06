"""
48 ms runtime beats 44.18%
16.3 MB memory beats 70.27%
"""
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        cnt = s.count(goal[0])
        t = -1
        for _ in range(cnt):
            t = s.find(goal[0], t+1)
            if s[t:] + s[:t] == goal:
                return True
        return False
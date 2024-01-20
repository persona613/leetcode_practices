"""
745 ms runtime beats 20.41%
32.12 MB memory beats 62.27%
"""
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        for d, s in zip(dist, speed):
            time.append(d/s)
        time = sorted(time)
        ans = 0
        for i, t in enumerate(time):
            if i < t:
                ans += 1
            else:
                break
        return ans
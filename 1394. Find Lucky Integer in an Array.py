"""
57 ms runtime beats 83.97%
16.4 MB memory beats 52.63%
"""
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dc = Counter(arr)
        ans = []
        for k in dc:
            if k == dc[k]:
                ans.append(k)
        return max(ans) if ans else -1
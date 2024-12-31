"""
78 ms runtime beats 35.18%
16.73 MB memory beats 75.33%
"""
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        t = 0
        for a in arr:
            if d[a] == 1:
                t += 1
                if t == k:
                    return a
        return ""
"""
1012 ms runtime beats 37.70%
26.76 MB memory beats 69.79%
"""
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        remain = mean * (m + n) - sum(rolls)
        if remain < n or remain > 6 * n:
            return []
        
        k = remain // n
        res = [k] * n
        for i in range(remain % n):
            res[i] += 1
        return res
"""
499 ms runtime beats 98.37%
29.98 MB memory beats 63.04%
"""
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n: return max(arr)
        # w=winner, i=challenger, r=round
        w = arr[0]
        r = 0
        for i in range(1, n):
            if arr[i] > w:
                w = arr[i]
                r = 1
            else:
                r += 1
            if r == k:
                return w
        return w
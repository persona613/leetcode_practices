"""
942 ms runtime beats 50.17%
69.00 MB memory beats 47.80%
"""
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        q = []
        for i in range(n - 1):
            a = arr[i]
            for j in range(i + 1, n):
                b = arr[j]
                q.append((a / b, a, b))
        q.sort()
        return q[k - 1][1:]
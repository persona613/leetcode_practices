"""
476 ms runtime beats 83.87%
30.35 MB memory beats 73.50%
"""
class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        # remain freq
        rf = [0] * k
        for a in arr:
            rf[a % k] += 1
        for i in range(k // 2 + 1):
            if i == 0 or i == k - i:
                if rf[i] % 2 == 1:
                    return False
            elif rf[i] != rf[k - i]:
                return False
        return True
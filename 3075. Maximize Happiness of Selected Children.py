"""
820 ms runtime beats 40.17%
43.60 MB memory beats 33.89%
"""
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        arr = sorted(happiness, reverse = True)
        print(len(arr))
        ans = 0
        for i in range(k):
            ans += max(0, arr[i] - i)
        return ans
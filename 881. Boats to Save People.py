"""
334 ms runtime beats 96.76%
23.45 MB memory beats 28.58%
"""
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i = 0
        j = len(people) - 1
        arr = sorted(people)
        ans = 0
        while i <= j:
            if arr[i] + arr[j] <= limit:
                i += 1
            j -= 1
            ans += 1
        return ans
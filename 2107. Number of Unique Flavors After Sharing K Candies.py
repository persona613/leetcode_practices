"""
136 ms runtime beats 28.50%
35.48 MB memory beats 59.12%
"""
class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        fs = Counter(candies)
        if k == 0: return len(fs)

        # init sliding window
        for i in range(k):
            fs[candies[i]] -= 1
            if fs[candies[i]] == 0:
                del fs[candies[i]]
        ans = len(fs)

        for i in range(k, len(candies)):
            fs[candies[i]] -= 1
            if fs[candies[i]] == 0:
                del fs[candies[i]]

            fs[candies[i - k]] += 1
            ans = max(ans, len(fs))
        return ans
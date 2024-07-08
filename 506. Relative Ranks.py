"""
56 ms runtime beats 93.52%
17.98 MB memory beats 22.65%
"""
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arr = []
        for i, val in enumerate(score):
            arr.append((val, i))
        arr.sort(reverse = True)

        n = len(arr)
        res = [None] * n
        for i in range(min(3, n)):
            if i == 0:
                r = "Gold Medal"
            elif i == 1:
                r = "Silver Medal"
            elif i == 2:
                r = "Bronze Medal"
            res[arr[i][1]] = r
            
        for i, t in enumerate(arr[3:], 4):
            res[t[1]] = str(i)
        return res
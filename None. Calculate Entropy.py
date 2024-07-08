"""
39 ms runtime beats None %
16.7 MB memory beats None %
"""
class Solution:
    def calculateEntropy(self, input: List[int]) -> float:
        n = len(input)
        cnt = Counter(input)
        for key in cnt:
            cnt[key] = cnt[key] / n
        return sum(map(lambda x: -x*math.log(x, 2), cnt.values()))
        
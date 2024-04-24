"""
53 ms runtime beats 85.14%
16.61 MB memory beats 75.09%
"""
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = defaultdict(int)
        for word in words:
            d[word] += 1

        n = len(words)
        bucket = [[] for _ in range(n + 1)]
        for word in d:
            freq = d[word]
            heapq.heappush(bucket[freq], word)

        res = []
        i = n
        while len(res) < k:
            if bucket[i]:
                res.append(heapq.heappop(bucket[i]))
            else:
                i -= 1
        return res

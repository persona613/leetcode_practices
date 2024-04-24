"""
Wrong Answer
32 / 110 testcases passed

Input
words =
["aaa","aa","a"]
k =
2

Use Testcase
Output
["a","aaa"]
Expected
["a","aa"]
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
        for i in range(n, 0, -1):
            if not bucket[i]:
                continue
            
            # k-len(res) = needed words to find
            if k - len(res) <= len(bucket[i]):
                res.extend(bucket[i][:k - len(res)])
                break
            else:
                res.extend(bucket[i])
        return res

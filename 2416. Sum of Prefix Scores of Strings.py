"""
1238 ms runtime beats 95.17%
212.56 MB memory beats 92.41%
"""
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = dict()
        for word in words:
            curr = trie
            for c in word:
                curr = curr.setdefault(c, dict())
                curr["counter"] = curr.get("counter", 0) + 1

        n = len(words)
        res = [0] * n
        for i in range(n):
            curr = trie
            cnt = 0
            for c in words[i]:
                curr = curr[c]
                cnt += curr["counter"]
            res[i] = cnt
        return res
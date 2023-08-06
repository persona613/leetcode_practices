"""
106 ms runtime beats 45.86%
16.5 MB memory beats 72.84%
"""
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans, mi = "a" * 16, 0
        dic = defaultdict(int)
        for c in licensePlate:
            if c.isalpha():
                dic[c.lower()] += 1
                mi += 1
        for word in words:
            tdic = dic.copy()
            i = 0
            while tdic and i < len(word):
                if word[i] in tdic:
                    tdic[word[i]] -= 1
                    if tdic[word[i]] == 0:
                        del tdic[word[i]]
                i += 1
            if not tdic and len(word) < len(ans):
                if len(word) == mi: return word
                ans = word
        return ans
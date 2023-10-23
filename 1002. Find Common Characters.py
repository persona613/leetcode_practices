"""
51 ms runtime beats 91.12%
16.5 MB memory beats 47.50%
"""
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dic = Counter(words[0])
        for i in range(1, len(words)):
            mi = Counter(words[i])
            dic = { k:min(dic[k], mi[k]) for k in set(dic)&set(mi)}
        return [ k for k, v in dic.items() for i in range(v)]

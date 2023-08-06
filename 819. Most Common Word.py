"""
50 ms runtime beats 74.16%
16.4 MB memory beats 25.25%
"""
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        symbols = "!?',;."
        for sym in symbols:
            if sym in paragraph:
                paragraph = paragraph.replace(sym, " ")
        para = paragraph.split()
        dic = defaultdict(int)
        for word in para:
            if word.islower():
                dic[word] += 1
            else:
                dic[word.lower()] += 1
        keys = sorted(dic, key=lambda x: dic[x], reverse=True)
        print(keys)
        for k in keys:
            if k not in banned:
                return k
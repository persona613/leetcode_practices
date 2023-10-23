"""
164 ms runtime beats 54.90%
17 MB memory beats 35.22%
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cmap = Counter(chars)
        ans = 0
        for w in words:
            wmap = Counter(w)
            for k, v in wmap.items():
                if v > cmap[k]:
                    break
            else:
                ans += len(w)
        return ans
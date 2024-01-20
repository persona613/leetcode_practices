"""
122 ms runtime beats 67.68%
16.73 MB memory beats 83.02%
"""
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cmap = Counter(chars)
        ans = 0
        for w in words:
            ws = set(w)
            for c in ws:
                if w.count(c) > cmap[c]:
                    break
            else:
                ans += len(w)
        return ans
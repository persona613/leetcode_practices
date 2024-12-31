"""
255 ms runtime beats 83.33%
27.85 MB memory beats 94.74%
"""
class Trie:

    def __init__(self):
        self.root = dict()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.setdefault(c, dict())
            curr["cnt"] = curr.get("cnt", 0) + 1

    def countWordsEqualTo(self, word: str) -> int:
        curr = self.root
        for c in word:
            if c not in curr:
                return 0
            curr = curr[c]

        paths = curr["cnt"]
        for c in curr:
            if c == "cnt":
                continue
            paths -= curr[c]["cnt"]
        return paths

    def countWordsStartingWith(self, prefix: str) -> int:
        curr = self.root
        for c in prefix:
            if c not in curr:
                return 0
            curr = curr[c]
        return curr["cnt"]

    def erase(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr[c]["cnt"] -= 1
            if curr[c]["cnt"] == 0:
                del curr[c]
                break
            curr = curr[c]


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)
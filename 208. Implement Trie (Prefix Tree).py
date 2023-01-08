"""
264 ms runtime beats 58%
36 MB memory beats 5.23%
"""
class Trie:

    def __init__(self, val=None):
        self.val = val
        self.children = [None]*26
        self.flag = False

    def insert(self, word: str) -> None:
        curr = self
        for i, c in enumerate(word):
            if not curr.children[ord(c)-ord("a")]:
                curr.children[ord(c)-ord("a")] = Trie(word[:i+1])
            curr = curr.children[ord(c)-ord("a")]
        curr.flag = True

    def search(self, word: str) -> bool:
        curr = self
        for c in word:
            if not curr.children[ord(c)-ord("a")]:
                return False
            curr = curr.children[ord(c)-ord("a")]        
        return curr.flag

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for c in prefix:
            if not curr.children[ord(c)-ord("a")]:
                return False
            curr = curr.children[ord(c)-ord("a")]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
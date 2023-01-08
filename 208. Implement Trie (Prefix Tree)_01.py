"""
Submission Result: Wrong Answer 
Input:
["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
Output:
[null,null,null,null,null,null,null,false,false,false,false,false,false,false,true,true,false,false,true,false,false,false,true,true,true]
Expected:
[null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,true,true,false,false,false,true,true,true]
"""
class Trie:

    def __init__(self, val=None):
        self.val = val
        self.children = [None]*26
        self.flag = False

    def insert(self, word: str) -> None:
        curr = self
        for i, c in enumerate(word):
            if c not in curr.children:
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
"""
553 ms runtime beats 69.02%
37.57 MB memory beats 52.53%
"""
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        # pick bag[0]=square(0,0)
        # pick bag[1]=square(1,1) with prefix bag[0][1]
        # pick bag[2]=square(2,2) with prefix bag[0][2], bag[1][2]
        # pick bag[3]=square(3,3) with prefix bag[0][3], bag[1][3], bag[2][3]

        def backtrack(k, n, bag):
            if k == n:
                res.append(bag[:])
                return
            prefix = make_prefix(k, bag)
            candidates = trie.search(prefix)
            for candidate in candidates:
                bag.append(candidate)
                backtrack(k + 1, n, bag)
                bag.pop()

        def make_prefix(k, bag):
            pre = []
            for i in range(k):
                pre.append(bag[i][k])
            return pre

        n = len(words[0])
        trie = Trie(words)
        res = []
        bag = []
        backtrack(0, n, bag)
        return res

class TrieNode:
    def __init__(self):
        self.link = dict()
        self.box = set()

class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.root.box = set(words)
        for word in words:
            self.insert(word)
    
    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.link:
                curr.link[c] = TrieNode()
            curr = curr.link[c]
            curr.box.add(word)
    
    def search(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.link:
                return []
            curr = curr.link[c]
        return curr.box
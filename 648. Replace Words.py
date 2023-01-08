"""
174 ms runtime beats 78.25%
35.9 MB memory beats 27.99%
"""
class TrieNode:
    def __init__(self):
        self.dict = {}
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.dict.setdefault(c, TrieNode())
        curr.end = True
    def replace(self, successor):
        curr = self.root
        root = ""
        for c in successor:
            if c not in curr.dict:
                return
            curr = curr.dict[c]
            root += c
            if curr.end:
                return root

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = Trie()
        for root in dictionary:
            tree.insert(root)
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if rt := tree.replace(word):
                words[i] = rt
        return " ".join(words)
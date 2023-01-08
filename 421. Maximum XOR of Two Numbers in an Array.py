"""
8949 ms runtime beats 5.19%
144.2 MB memory beats 12.16%
"""
class TrieNode:
    
    def __init__(self):
        self.children = {}
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, TrieNode())
            
    def find_approximate(self, word):
        res = ""
        curr = self.root
        for c in word:
            if c not in curr.children:
                c = str((int(c)+1)%2)
            curr = curr.children[c]
            res += c
        return res        

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ptree = Trie()
        for n in nums:
            ptree.insert(f"{n:032b}")
            
        res = 0
        m = int("1"*32, 2)
        for n in nums:
            a = ptree.find_approximate(f"{n^m:032b}")
            res = max(res, int(a, 2)^n)            
        return res
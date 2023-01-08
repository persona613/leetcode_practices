"""
Submission Result: Wrong Answer 
Input:
["a","abc","aba",""]
Output:
[[3,0],[3,1],[3,2],[0,2],[0,3],[1,3],[2,3]]
Expected:
[[0,3],[3,0],[2,3],[3,2]]
"""
class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = False
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, TrieNode())
        curr.end = True
    
    def search_invert(self, word):
        curr = self.root
        res = []
        iword = ""
        if curr.end: 
            res.append("")
        
        for i in range(-1, -len(word)-1, -1):
            if word[i] not in curr.children:
                return res
            curr = curr.children[word[i]]
            iword += word[i]
            if curr.end and iword != word:
                res.append(iword)
        return res
            
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ptree = Trie()
        for wd in words:
            ptree.insert(wd)
        res = []
        
        for i, wd in enumerate(words):
            if wd == "":
                for j in range(len(words)):
                    if j == i:
                        continue
                    res.append([j,i])
                    
            elif iwords := ptree.search_invert(wd):
                for iwd in iwords:
                    j = words.index(iwd)
                    res.append([j,i])
        return res
            
        
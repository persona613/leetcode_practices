"""
3550 ms runtime beats 73.56%
316 MB memory beats 24.56%
"""

class TrieNode:

    def __init__(self):
        self.children = {}
        self.end = None # record word's index
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, index):
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, TrieNode())
        curr.end = index
    
    def search_invert(self, word):
        curr = self.root
        res = []
        iword = ""       
        for i in range(-1, -len(word)-1, -1):
            if word[i] not in curr.children:
                return res
            curr = curr.children[word[i]]
            iword += word[i]
            if curr.end != None:
                if self.check_palindrome(iword, word, 0, i-1+len(word), key=1):
                    res.append(curr.end)
        
        # while left word's len > right word's len
        # continue run left word index(= iword's surfix word)
        # find words with same prefix(= iword)
        if other_iwords := self.search_allsurfix(curr, iword, iword):
            res.extend(other_iwords)
        return res
    
    def check_palindrome(self, iword, word, li, ri, key=1):
        if iword == word: # unique strings words
            return False
        curr = word     
        if key == 0 or word == "": # if k=1, search right word, k=0 search left iword
            curr = iword
            
        while li <= ri:
            if curr[li] != curr[ri]:
                return False
            li += 1
            ri -= 1
        return True
    
    def search_allsurfix(self, node, tmpword, prefix):
        res = []
        if not node.children:
            return res        
        curr = node
        surfixword = tmpword
        for k in node.children:
            curr = node.children[k]
            surfixword += k
            if curr.end != None:
                if self.check_palindrome(surfixword, prefix, len(prefix), len(surfixword)-1, key=0):
                    res.append(curr.end)
            if surfixwords := self.search_allsurfix(curr, surfixword, prefix):
                res.extend(surfixwords) 
            surfixword = surfixword[:-1]
        return res
                
        
            
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ptree = Trie()
        for i, wd in enumerate(words):
            ptree.insert(wd, i)
        res = []

        for i, wd in enumerate(words):
            if wd == "":
                for j in range(len(words)):
                    if ptree.check_palindrome(words[j], wd, 0, len(words[j])-1, key=0):
                        res.extend([[j,i],[i,j]])
                    
            elif iwords_index := ptree.search_invert(wd):
                for j in iwords_index:
                    res.append([j,i])
        return res
            
        
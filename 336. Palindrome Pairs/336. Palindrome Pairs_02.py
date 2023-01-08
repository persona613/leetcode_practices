"""
Submission Result: Wrong Answer 
Input:
["a","b","c","ab","ac","aa"]
Output:
[[1,3],[2,4],[0,5]]
Expected:
[[3,0],[1,3],[4,0],[2,4],[5,0],[0,5]]
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
            if self.check_palindrome(iword, word, 0, len(word)-1):
                res.append(iword)
        
        for i in range(-1, -len(word)-1, -1):
            if word[i] not in curr.children:
                return res
            curr = curr.children[word[i]]
            iword += word[i]
            if curr.end:
                if self.check_palindrome(iword, word, 0, len(word)+i-1):
                    res.append(iword)
        return res
    
    def check_palindrome(self, iword, word, li, ri):
        if iword == word: # unique strings words
            return False
        curr = word     
        if word == "":
            curr = iword
            
        while li <= ri:
            if curr[li] != curr[ri]:
                return False
            li += 1
            ri -= 1
        return True
            
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        ptree = Trie()
        for wd in words:
            ptree.insert(wd)
        res = []
        
        for i, wd in enumerate(words):
            if wd == "":
                for j in range(len(words)):
                    if ptree.check_palindrome(words[j], wd, 0, len(words[j])-1):
                        res.append([j,i])
                    
            elif iwords := ptree.search_invert(wd):
                for iwd in iwords:
                    j = words.index(iwd)
                    res.append([j,i])
        return res
            
        
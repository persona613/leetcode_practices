"""
9589 ms runtime beats 60.26%
78.2 MB memory beats 25.9%
"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            curr = curr.children.setdefault(c, TrieNode())
        curr.end = True

    def search(self, word: str) -> bool:
        return self.dfs(self.root, word, 0)
    
    def dfs(self, node, word, i):
        # base case
        if i == len(word):
            return node.end

        # recurrent relation
        if word[i] in node.children:
            return self.dfs(node.children[word[i]], word, i+1)
        elif word[i] == ".":
            for k in node.children.keys():
                if self.dfs(node.children[k], word, i+1):
                    return True
                
        return False # enclude word[i] not in node.children:
        
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
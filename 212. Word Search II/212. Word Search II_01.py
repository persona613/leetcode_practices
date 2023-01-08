"""
Submission Result: Wrong Answer 
Input:
[["a","a"]]
["aaa"]
Output:
["aaa"]
Expected:
[]
"""
class TrieNode:
    
    def __init__(self):
        self.children = {}
        
class Trie:
    
    # { char : {(i,j):TrieNode()} }
    def __init__(self, board=None):
        self.root = TrieNode()
        self.board = board
        
    # t = (i,j)  
    def insert_cell(self, t):
        node = self.root
        char = self.board[t[0]][t[1]]
        if char not in node.children:
            node.children[char] = {t:TrieNode()}
        elif t not in node.children[char]:
            node.children[char][t] = TrieNode()
        return node.children[char][t]
    
    def search_cell(self, node, t):
        char = self.board[t[0]][t[1]]
        if char not in node.children:
            return False
        elif t not in node.children[char]:
            return False
        return True
    
    def link_cell(self, node, t):        
        for d in [1,-1]:
            if 0<= t[0]+d and t[0]+d <len(self.board):
                nt = (t[0]+d,t[1])
                rownext = self.insert_cell(nt)
                char = self.board[nt[0]][nt[1]]
                if char not in node.children:
                    node.children[char] = {nt:rownext}
                elif nt not in node.children[char]:
                    node.children[char][nt] = rownext
                    
            if 0<= t[1]+d and t[1]+d <len(self.board[0]):
                nt = (t[0],t[1]+d)
                colnext = self.insert_cell(nt)
                char = self.board[nt[0]][nt[1]]
                if char not in node.children:
                    node.children[char] = {nt:colnext}
                elif nt not in node.children[char]:
                    node.children[char][nt] = colnext
                    
    def create_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                curr = self.insert_cell((i,j))
                self.link_cell(curr, (i,j))
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        btree = Trie(board)
        btree.create_board() 
        
        def dfs(node, word, i):
            if i == len(word):
                return True        
            if word[i] not in node.children:
                return False
            for cell in node.children[word[i]].values():
                if dfs(cell, word, i+1):
                    return True
            return False

        res = []    
        for word in words:
            if dfs(btree.root, word, 0):
                res.append(word)
        return res

        
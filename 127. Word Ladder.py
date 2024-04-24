"""
420 ms runtime beats 33.25%
17.60 MB memory beats 97.97%
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        def gen(word):
            for i in range(len(word)):
                curr = word[i]
                for c in als:
                    if c != curr:
                        yield word[:i] + c + word[i+1:]
                        
        if endWord not in wordList:
            return 0
        als = "abcdefghijklmnopqrstuvwxyz"
        wd = set(wordList)
        seen = {beginWord}
        q = deque([(beginWord, 1)])
        while q:
            curr, p = q.popleft()
            if curr == endWord:
                return p
            f = gen(curr)
            while True:
                nxt = next(f, None)
                if not nxt:
                    break
                if nxt in wd and nxt not in seen:
                    seen.add(nxt)
                    q.append((nxt, p + 1))
        return 0
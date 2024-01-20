"""
119 ms runtime beats 5.08%
17.59 MB memory beats 9.52%
"""
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        cnt = 0
        for wd in words:
            cnt += len(wd)
        if cnt % n:
            return False

        fr = defaultdict(int)
        for wd in words:
            for c in wd:
                fr[c] += 1
        for k in fr:
            if fr[k] % n:
                return False
        return True
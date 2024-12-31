"""
179 ms runtime beats 7.72%
19.85 MB memory beats 96.57%
"""
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:

        def abbr(mask):
            abb = []
            k = 0
            for i in range(n):
                bit = 1 << (n - 1 - i)
                if mask & bit:
                    k += 1
                else:
                    if k:
                        abb.append(str(k))
                        k = 0
                    abb.append(word[i])
            if k:
                abb.append(str(k))
            return "".join(abb)

        n = len(word)
        res = []
        for i in range(2 ** n):
            res.append(abbr(i))
        return res

        # -------------------------------
        # index, bitmask
        # def backtrack(i, mask):
        #     if i == n:
        #         res.append(mask)
        #         return
            
        #     # not turn to int
        #     backtrack(i + 1, mask)
        #     # turn to int
        #     bit = 1 << (n - 1 - i)
        #     backtrack(i + 1, mask ^ bit)
            
        # n = len(word)
        # res = []
        # backtrack(0, 0)
        # for i in range(len(res)):
            # res[i] = abbr(res[i])
        # return res
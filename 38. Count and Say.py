"""
52 ms runtime beats 50%
14 MB memory beats 24.72%
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        def say(words):
            ans = ""
            j = 0
            prev = words[0]
            for i, d in enumerate(words):
                if d != prev:
                    # cnt = i-j
                    ans += str(i-j) + prev
                    j = i
                    prev = d
            ans += str(len(words)-j) + prev
            return ans

        memo = "1"
        for i in range(2, n+1):
            memo = say(memo)
        return memo
"""
44 ms runtime beats 12.67%
17.22 MB memory beats 7.80%
"""
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # dp: before decision
        @cache
        def dp(i, balance):
            if balance < 0:
                return False
            if i == len(s):
                if balance == 0:
                    return True
                return False

            c = s[i]
            if c == "(":
                return dp(i + 1, balance + 1)
            elif c == ")":
                return dp(i + 1, balance - 1)
            else:
                return dp(i + 1, balance + 1) or \
                       dp(i + 1, balance - 1) or \
                       dp(i + 1, balance)

        return dp(0, 0)
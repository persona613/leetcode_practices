"""
41 ms runtime beats 87.84%
16.3 MB memory beats 39.57%
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = -1, -1
        bi, bj = 0, 0 # backspace cnount
        lc, rc = "", ""
        while i > -len(s)-1 or j > -len(t)-1:
            while i > -len(s)-1:
                if s[i] == "#":
                    bi += 1
                elif bi > 0:
                    bi -= 1
                else:
                    lc = s[i]
                    break
                i -= 1
            else:
                lc = ""
            while j > -len(t)-1:
                if t[j] == "#":
                    bj += 1
                elif bj > 0:
                    bj -= 1
                else:
                    rc = t[j]
                    break
                j -= 1
            else:
                rc = ""
            if lc != rc:
                return False
            i -= 1
            j -= 1
        return True
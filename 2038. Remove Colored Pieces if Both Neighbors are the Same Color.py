"""
95 ms runtime beats 98.26%
17.3 MB memory beats 65.73%
"""
class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        A = B = cnt = 0
        g = colors[0]
        for c in colors:
            if c == g:
                cnt += 1
            else:
                if cnt >= 3:
                    if g == "A":
                        A += cnt-2
                    else:
                        B += cnt-2
                g = c
                cnt = 1
        if cnt >= 3:
            if g == "A":
                A += cnt-2
            else:
                B += cnt-2
        return A > B
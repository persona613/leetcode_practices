"""
129 ms runtime beats 5.91%
17.46 MB memory beats 5.69%
"""
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        j = 0
        t = 1
        for i in range(1, n):
            if chars[i] != chars[i - 1]:
                chars[j] = chars[i - 1]
                j += 1
                if t > 1:
                    for s in str(t):
                        chars[j] = s
                        j += 1
                t = 1
            else:
                t += 1
        chars[j] = chars[-1]
        j += 1
        if t > 1:
            for s in str(t):
                chars[j] = s
                j += 1
        for _ in range(n - j):
            chars.pop()
        return len(chars)
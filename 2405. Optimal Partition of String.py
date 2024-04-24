"""
86 ms runtime beats 69.29%
17.42 MB memory beats 32.08%
"""
class Solution:
    def partitionString(self, s: str) -> int:
        bag = set()
        ans = 1
        for c in s:
            if c in bag:
                bag = {c}
                ans += 1
            else:
                bag.add(c)
        return ans
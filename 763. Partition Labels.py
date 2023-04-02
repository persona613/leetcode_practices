"""
45 ms runtime beats 61.65%
13.8 MB memory beats 97.2%
"""
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maps = {}
        for i, c in enumerate(s):
            if i > maps.setdefault(c, -1):
                maps[c] = i
        ans = []
        i = 0
        label = 0
        cnt = 0
        for i in range(len(s)):
            if maps[s[i]] > label:
                label = maps[s[i]]
            cnt += 1
            if i == label:
                ans.append(cnt)
                cnt = 0
        return ans
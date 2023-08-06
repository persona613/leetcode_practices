"""
61 ms runtime beats 8.52%
16.5 MB memory beats 89.54%
"""
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        cnt, sset, gset = 0, set(), set()
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] += 1
            if s[i] != goal[i]:
                cnt += 1
                sset.add(s[i])
                gset.add(goal[i])
        if cnt == 0:
            for v in dic.values():
                if v >= 2:
                    return True
            return False
        elif cnt == 2:
            return sset == gset
        return False
"""
37 ms runtime beats 81.42%
16.65 MB memory beats 49.11%
"""
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:

        def find_parent(i):
            if parents[i] != i:
                parents[i] = find_parent(parents[i])
            return parents[i]
        
        def union(t1, t2):
            p1 = find_parent(t1)
            p2 = find_parent(t2)
            if p1 == p2:
                return
            if p1 < p2:
                parents[p2] = parents[p1]
            else:
                parents[p1] = parents[p2]

        # UnionFind
        parents = [i for i in range(26)]
        for i in range(len(s1)):
            t1 = ord(s1[i]) - ord("a")
            t2 = ord(s2[i]) - ord("a")
            union(t1, t2)

        res = []
        for c in baseStr:
            t = ord(c) - ord("a")
            p = find_parent(t)
            res.append(chr(p + ord("a")))
        return "".join(res)
"""
47 ms runtime beats 6.20%
16.56 MB memory beats 75.68%
"""
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 1:
            return "".join(set(words[0]))

        def check(i, a, b):
            for c in a[i:]:
                if c not in indegree:
                    indegree[c] = 0
            for c in b[i:]:
                if c not in indegree:
                    indegree[c] = 0

        def compare(a, b):
            asize = len(a)
            bsize = len(b)
            for i in range(min(asize, bsize)):
                u = a[i]
                v = b[i]
                if u != v:
                    if v not in gf[u]:
                        gf[u].add(v)
                        indegree[v] += 1
                        if u not in indegree:
                            indegree[u] = 0

                        # any position
                        # register other chars in indegree
                        check(i + 1, a, b)
                    break
                else:
                    # any position
                    if u not in indegree:
                        indegree[u] = 0
            else:
                if asize > bsize:
                    return False
                else:
                    # any position
                    for i in range(asize, bsize):
                        u = b[i]
                        if u not in indegree:
                            indegree[u] = 0
            return True

        # kahn's algorithm
        # {u -> [v]}
        gf = defaultdict(set)
        indegree = defaultdict(int)
        n = len(words)
        for i in range(len(words) - 1):
            curr = words[i]
            for j in range(i + 1, n):
                suf = words[j]
                ret = compare(curr, suf)
                if ret is False:
                    return ""
        # print(f"{indegree = }")
        # print(gf)

        q = deque([c for c in indegree if indegree[c] == 0])
        # print(q)
        res = []
        while q:
            curr = q.popleft()
            res.append(curr)
            for adj in gf[curr]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    q.append(adj)
        # print(res)
        return "".join(res) if len(res) == len(indegree) else ""
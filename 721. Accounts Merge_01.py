"""
Wrong Answer
12 / 50 testcases passed

Editorial
Input
accounts =
[["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]]

Use Testcase
Output
[]
Expected
[["David","David0@m.co","David1@m.co","David3@m.co","David4@m.co","David5@m.co"]]
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def root(i):
            if parents[i] != i:
                parents[i] = root(parents[i])
            return parents[i]

        def is_common(i, j):
            ri = root(i)
            rj = root(j)
            if len(mails[ri]) > len(mails[rj]):
                return is_common(rj, ri)

            for mail in mails[ri]:
                if mail in mails[rj]:
                    return True
            return False
        
        def union(i, j):
            ri = root(i)
            rj = root(j)
            if len(mails[ri]) >= len(mails[rj]):
                parents[rj] = parents[ri]
                mails[ri] = mails[ri].union(mails[rj])
                mails[rj] = set()
            else:
                parents[ri] = parents[rj]
                mails[rj] = mails[rj].union(mails[ri])
                mails[ri] = set()

        n = len(accounts)
        # Union Find
        parents = list(range(n))
        names = []
        mails = []
        for acc in accounts:
            names.append(acc[0])
            mails.append(set(acc[1:]))

        for i in range(n):
            for j in range(i + 1, n):
                # check same name and common mails
                if names[i] != names[j]:
                    continue
                if is_common(i, j):
                    union(i, j)
        res = []
        for i in range(n):
            if len(mails[i]) > 0:
                res.append([names[i]] + sorted(mails[i]))
        return res
        
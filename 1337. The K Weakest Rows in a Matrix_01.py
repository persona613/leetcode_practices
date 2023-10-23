"""
Wrong Answer
31 / 52 testcases passed
Input
mat = [[1,0],[1,0],[1,0],[1,1]]
k = 4

Use Testcase
Output
[3,0,1,2]
Expected
[0,1,2,3]
"""
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def bs(row, n):
            l, r = 0, n-1
            while l < r:
                m = (l+r)//2
                if row[m] == 0:
                    if m-1>=0 and row[m-1]==1:
                        return m
                    r = m-1
                else:
                    if m+1<n and row[m+1]==0:
                        return m+1
                    l = m+1
            return 0 if m==0 else n
        
        n = len(mat[0])
        # (cnt, index)
        lt = sorted([(bs(row, n), i) for i, row in enumerate(mat)])
        return [lt[i][1] for i in range(k)]


        # n = len(mat[0])
        # lt = [] # (cnt, index)
        # for i, row in enumerate(mat):
        #     if row[-1] == 1:
        #         lt.append((n, i))
        #     else:
        #         lt.append((row.index(0), i)) # 1's cnt
        # lt.sort()
        # return [lt[i][1] for i in range(k)]
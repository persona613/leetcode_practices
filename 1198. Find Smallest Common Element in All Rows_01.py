"""
Wrong Answer
12 / 13 testcases passed

Editorial
Input
mat =
[[10,2075,2700,3884,5017,6177,6829,8294,8695,9263],[262,889,1873,2700,5413,6039,6491,6501,7525,8294],[1348,1504,2950,6107,6747,7003,8294,8355,8601,9412],[2616,4624,5788,6115,7401,7461,7525,7840,7886,8294],[1739,2002,4239,5151,5238,6190,6848,7238,7722,8294],[4118,4551,5470,6114,7672,7975,8294,8971,9080,9656],[195,2418,5963,6151,7720,7865,8294,8417,8729,9852],[1195,2657,3608,4285,5154,5299,5497,6960,8125,8294],[511,934,3065,3227,3290,3988,4969,7846,8294,9228],[641,1489,2888,3727,4453,5527,6146,6459,8294,9567]]

Use Testcase
Output
-1
Expected
8294
"""
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cads = deque(mat[0])
        m = len(mat)
        n = len(mat[0])
        for i in range(1, m):
            if not cads:
                return -1

            # binary search start index
            j = 0
            for _ in range(len(cads)):
                curr = cads.popleft()
                j = bisect.bisect_left(mat[i], curr, j, n - 1)
                if j == n:
                    break
                if mat[i][j] == curr:
                    cads.append(curr)
                    j += 1
        return min(cads) if cads else -1
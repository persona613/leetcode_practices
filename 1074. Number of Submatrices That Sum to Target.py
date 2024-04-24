"""
640 ms runtime beats 48.76%
17.50 MB memory beats 82.23%
"""
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        ans = 0
        m = len(matrix)
        n = len(matrix[0])
        # col presum
        mt = copy.deepcopy(matrix)
        for i in range(1, m):
            for j in range(n):
                mt[i][j] += mt[i-1][j]
        
        # calculate submatrix, st=start i
        # dic = {sum of submatrix : count}
        # curr = presum on fly
        for si in range(m):
            for i in range(si, m):
                dic = defaultdict(int)
                dic[0] = 1
                curr = 0
                for j in range(n):
                    if si == 0:
                        curr += mt[i][j]
                    else:
                        curr += mt[i][j] - mt[si-1][j]
                    ans += dic[curr - target]
                    dic[curr] += 1
        return ans

"""
Wrong Answer
42 / 48 testcases passed
"""
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        md = 10**9 + 7
        ans = 1
        memo = defaultdict(int)
        memo[arr[0]] = 1
        for i in range(1, n):
            a = arr[i]
            cnt = 1
            for j in range(i):
                d = arr[j]
                if a % d == 0:
                    cnt += memo[d] * memo[a//d] % md
            memo[a] = cnt
            ans += cnt
        return ans
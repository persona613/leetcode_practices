"""
1775 ms runtime beats 5.04%
196.67 MB memory beats 6.12%
"""
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def dfs(i, v, d):
            if (i, v, d) in memo:
                return memo[(i, v, d)]
            if i == 2 and d == None:
                if nums[2] - nums[1] == nums[1] - nums[0]:
                    ans = 1
                else:
                    ans = 0
                memo[(i, v, d)] = ans
                return ans
            if i < 2 and d == None:
                memo[(i, v, d)] = 0
                return 0
            
            if d != None:
                ans = 0
                pre = v - d
                for idx in ip[pre]:
                    if idx < i:
                        ans += dfs(idx, pre, d) + 1
            else:
                # not take nums[i]
                ans = dfs(i-1, nums[i-1], None)
                # print("not take nums[i]:",(i-1, nums[i-1], None), ans)
                
                # take nums[i]
                for j in range(i-1, -1, -1):
                    pre = nums[j]
                    ans += dfs(j, pre, v-pre)
                    # print("take nums[i]:",(j, pre, v-pre), ans)
            memo[(i, v, d)] = ans
            return ans

        memo = dict()
        n = len(nums)
        ip = defaultdict(list)
        for i, v in enumerate(nums):
            ip[v].append(i)
        # ret = dfs(n-1, nums[-1], None)
        # print(memo)
        # return ret
        return dfs(n-1, nums[-1], None)
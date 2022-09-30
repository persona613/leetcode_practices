'''
Time Limit Exceeded
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        cnt = 0
        ans = []
        tmpsum = 0
        while i < len(nums):
            j = i
            cnt = 0
            tmpsum = 0
            while j < len(nums):
                tmpsum += nums[j]
                cnt += 1                
                if tmpsum >= target:
                    if cnt == 1:
                        return 1
                    ans.append(cnt)
                    # print(ans)
                    break
                j += 1
            if len(ans) == 0:
                return 0
            i += 1
        # print(ans)
        return min(ans)
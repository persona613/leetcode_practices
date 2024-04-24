"""
342 ms runtime beats 60.83%
20.12 MB memory beats 29.82%
"""
class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        # at_most_count(k) - at_most_count(k-1)
        def count(t, n):
            if t == 0: return 0
            dic = defaultdict(int)
            i = ans = 0
            for j in range(n):
                dic[nums[j]] += 1
                while len(dic) > t:
                    if dic[nums[i]] == 1:
                        del dic[nums[i]]
                    else:
                        dic[nums[i]] -= 1
                    i += 1
                ans += j - i + 1
            return ans

        n = len(nums)
        return count(k, n) - count(k - 1, n)
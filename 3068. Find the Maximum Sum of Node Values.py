"""
925 ms runtime beats 97.62%
28.28 MB memory beats 39.29%
"""
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n = len(nums)
        flipcard = 0
        xred = []
        for x in nums:
            xred.append((x ^ k) - x)
            if xred[-1] > 0:
                flipcard += 1

        ans = sum(nums)
        if flipcard == 0:
            return ans

        xred.sort(reverse = True)
        if flipcard == 1:
            flipscore = xred[0] + xred[1]
            if flipscore > 0:
                return ans + flipscore
            return ans

        # add postive score every pair
        for t in range(0, flipcard - 1, 2):
            ans += xred[t] + xred[t + 1]

        # if flipcard is odd
        nxt = t + 2
        if nxt < n and nxt + 1 < n:
            flipscore = xred[nxt] + xred[nxt + 1]
            if flipscore > 0:
                ans += flipscore
        return ans
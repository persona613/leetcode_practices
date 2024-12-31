"""
435 ms runtime beats 65.63%
16.57 MB memory beats 92.36%
"""
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        cnt = 0
        # dp: count less than curr i
        less = [0] * n
        # dp: count greater than curr i
        great = [0] * n
        for i in range(n):
            curr = rating[i]
            for j in range(i):
                if rating[j] < curr:
                    # count elements less than curr
                    less[i] += 1
                    # find j as second big, count teams
                    cnt += less[j]
                if rating[j] > curr:
                    # count elements greater than curr
                    great[i] += 1
                    # find j as second small, count teams
                    cnt += great[j]
        return cnt
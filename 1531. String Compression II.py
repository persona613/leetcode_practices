"""
4380 ms runtime beats 6.85%
358.57 MB memory beats 44.95%
"""
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        memo = dict()
        ls = [1, 9, 99]

        def take(i, d, pchar, pcnt):
            if (i, d, pchar, pcnt) in memo:
                return memo[(i, d, pchar, pcnt)]
            if i == n:
                return 0

            curr = s[i]
            if curr == pchar:
                # take
                if pcnt in ls:
                    ret1 = take(i + 1, d, pchar, pcnt + 1) + 1
                else:
                    ret1 = take(i + 1, d, pchar, pcnt + 1)

                # not take
                ret2 = inf
                if d > 0:
                    ret2 = take(i + 1, d - 1, pchar, pcnt)
            else:
                # take
                ret1 = take(i + 1, d, curr, 1) + 1

                # not take
                ret2 = inf
                if d > 0:
                    ret2 = take(i + 1, d - 1, pchar, pcnt)
            memo[(i, d, pchar, pcnt)] = min(ret1, ret2)
            return memo[(i, d, pchar, pcnt)]
        # print(memo)
        return take(0, k, "", 0)






"""
106 ms runtime beats 32.29%
17.81 MB memory beats 93.70%
"""
class Solution:
    def largestPalindromic(self, num: str) -> str:
        ds = [0] * 10
        for d in num:
            ds[int(d)] += 1
        prehalf = []
        for i in range(9, -1, -1):
            if ds[i] > 1:
                if i == 0 and not prehalf:
                    break
                take = ds[i] // 2
                prehalf.append(str(i) * take)
                ds[i] -= take * 2
        oddmid = ""
        for i in range(9, -1, -1):
            if ds[i]:
                oddmid = str(i)
                break
        if not prehalf:
            return oddmid
        else:
            return "".join(prehalf) + oddmid + "".join(prehalf[::-1])

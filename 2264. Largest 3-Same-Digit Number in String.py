"""
47 ms runtime beats 31.79%
16.35 MB memory beats 24.76%
"""
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        bag = defaultdict(int)
        for i in range(3):
            bag[num[i]] += 1
        if len(bag) == 1:
            res = set(bag).pop()
        for i in range(3, len(num)):
            bag[num[i]] += 1
            pre = num[i-3]
            bag[pre] -= 1
            if bag[pre] == 0:
                del bag[pre]
            if len(bag) == 1:
                k = set(bag).pop()
                if k > res:
                    res = k
        return res * 3
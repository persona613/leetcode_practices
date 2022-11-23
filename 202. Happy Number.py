'''
Runtime: 63 ms, faster than 58.60% of Python3 online submissions 
Memory Usage: 13.8 MB, less than 97.10% of Python3 online submissions
'''

class Solution:
    def happynum(self, n: int) -> int:
        dg = str(n)
        newnum = 0
        for d in dg:
            newnum += int(d) ** 2
        return newnum
    def isHappy(self, n: int) -> bool:
        bucket = set()
        while True:
            n = self.happynum(n)
            if n == 1:
                return True
            elif n in bucket:
                return False
            else:
                bucket.add(n)
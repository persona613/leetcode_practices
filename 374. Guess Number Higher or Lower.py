"""
43 ms runtime beats 75.34%
14 MB memory beats 16%
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        st = 1
        en = n
        mi = (st+en) // 2
        
        while st < en:
            if guess(mi) == 0:
                return mi
            elif guess(mi) == -1:
                en = mi - 1
                mi = (st+en) // 2
            else:
                st = mi + 1
                mi = (st+en) // 2
        return mi
        
        
"""
Wrong Answer
216 / 217 testcases passed

Editorial
Input
n =
"9009"

Use Testcase
Output
"9119"
Expected
"8998"
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:

        def ispalindrome(s):
            l, r = 0, len(s) - 1
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        v = int(n)
        for d in [-1, 1, -2, 2]:
            if ispalindrome(str(v + d)):
                return str(str(v + d))

        arr = list(n)
        if ispalindrome(n):
            first = n
            diff = float("inf")
        else:
            # create first palindrome
            l, r = 0, len(arr) - 1
            while l < r:
                if arr[l] != arr[r]:
                    arr[r] = arr[l]
                l += 1
                r -= 1

            first = "".join(arr)
            diff = abs(int(first) - v)

        # test mid digits
        midx = len(arr) // 2
        a = int(arr[midx])
        for d in [1, -1]:
            na = (a + d) % 10
            arr[midx] = str(na)
            if len(arr) % 2 == 0:
                arr[midx - 1] = str(na)
            
            second = "".join(arr)
            newdiff = abs(int(second) - v)

            if newdiff < diff:
                first = second
                diff = newdiff
            elif newdiff == diff:
                if second < first:
                    first = second
                    diff = newdiff
        return first

        # if len(n) == 1:
        #     return str(int(n) - 1)

        # v = int(n)
        # # n = 10 ** k
        # if v % (10 ** (len(n) - 1)) == 0:
        #     return str(int(n) - 1)

        # # n = 99800
        # if n[-1] == "0":
        #     if ispalindrome(str(v - 1)):
        #         return str(v - 1)

        # # end of n = 1, 9
        # # n = 11, 101
        # if n[-1] == "1":
        #     if ispalindrome(str(v - 2)):
        #         return str(v - 2)
        # if n[-1] == "9":
        #     if ispalindrome(str(v + 2)):
        #         return str(v + 2)
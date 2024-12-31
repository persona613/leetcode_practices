"""
39 ms runtime beats 36.42%
16.57 MB memory beats 67.95%
"""
class Solution:
    def nearestPalindromic(self, n: str) -> str:

        def ispalindrome(s):
            if len(s) == 1: return True
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

        if len(n) <= 2:
            first = n
            diff = 100
            for i in range(1, 10):
                t = i * 10 + i
                if t == v:
                    continue
                newdiff = abs(t - v)
                if newdiff < diff:
                    diff = newdiff
                    first = str(t)
            return first

        # create first palindrome
        arr = list(n)
        ln = len(arr)
        l, r = 0, ln - 1
        while l < r:
            if arr[l] != arr[r]:
                arr[r] = arr[l]
            l += 1
            r -= 1

        first = "".join(arr)
        if first == n:
            diff = float("inf")
        else:
            diff = abs(int(first) - v)

        # test mid digits
        # if mid digits is 0, n = 9009,990099
        candidates = []
        midx = ln // 2
        if arr[midx] == "0":
            l = r = midx
            if ln % 2 == 0:
                l -= 1
            while r < ln and arr[r] == "0":
                l -= 1
                r += 1
            a = int(arr[r]) - 1
            second = first[:l] + str(a) \
                    + "9" * (r - l - 1) \
                    + str(a) + first[r + 1:]
            candidates.append(second)

        a = int(arr[midx])
        for d in [1, -1]:
            na = (a + d) % 10
            arr[midx] = str(na)
            if ln % 2 == 0:
                arr[midx - 1] = str(na)
            
            second = "".join(arr)
            candidates.append(second)
        
        # compare all candidates
        for second in candidates:
            newdiff = abs(int(second) - v)
            if newdiff < diff:
                first = second
                diff = newdiff
            elif newdiff == diff:
                if second < first:
                    first = second
                    diff = newdiff
        return first
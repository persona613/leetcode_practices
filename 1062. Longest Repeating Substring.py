"""
39 ms runtime beats 81.93%
16.94 MB memory beats 61.41%
"""
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:

        def search(arr, mod, base, power, k):
            if k == 0:
                return True
            
            pool = set()
            # first window string hash
            t = 0
            for i in range(k):
                # k-1-i, get power-d from reverse i
                t += arr[i] * power[k - 1 - i] % mod
            t %= mod
            pool.add(t)
            # Hightest digit power of length k is k-1
            for i in range(1, n - k + 1):
                t = (t - arr[i - 1] * power[k - 1] % mod) * base % mod \
                        + arr[i + k - 1]
                t %= mod
                if t < 0:
                    t += base
                if t in pool:
                    return True
                pool.add(t)
            return False

        # try Rabin-Karp's algorithm
        mod = 10 ** 9 + 7
        base = 26
        # turn s into int array
        arr = []
        for c in s:
            arr.append(ord(c) - ord("a"))
        
        # pre calculate every digit power
        n = len(s)
        power = []
        p = 1
        for d in range(n):
            power.append(p)
            p = (p * base) % mod

        # binary search
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if search(arr, mod, base, power, mid):
                l = mid + 1
            else:
                r = mid - 1
        return r
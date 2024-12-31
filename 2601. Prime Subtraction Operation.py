"""
249 ms runtime beats 10.05%
16.98 MB memory beats 12.98%
"""
class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = []
        for v in range(2, 1001):
            for f in range(2, int(v ** 0.5) + 1):
                if v % f == 0:
                    break
            else:
                primes.append(v)

        arr = nums[:]
        t = bisect.bisect_left(primes, arr[0]) - 1
        # edge case: arr[0] = 2
        if t >= 0:
            arr[0] -= primes[t]
        for i in range(1, len(arr)):
            t = bisect.bisect_left(primes, arr[i]) - 1
            while t >= 0 and arr[i] - primes[t] <= arr[i - 1]:
                t -= 1
                
            if t < 0:
                if arr[i] > arr[i - 1]:
                    continue
                else:
                    return False
            arr[i] -= primes[t]

        return True
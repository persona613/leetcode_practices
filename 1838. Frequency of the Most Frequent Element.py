"""
1176 ms runtime beats 45.86%
30.98 MB memory beats 85.94%
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        arr = sorted(nums)
        sizes = [1]
        i = 1
        j = 0
        n = len(arr)
        psum = arr[0]
        while i < n:
            diff = arr[i]-arr[i-1]
            width = i - j
            t = diff*width
            if k-t>=0:
                sizes.append(width+1)
                i += 1
                k -= t
            else:
                k += arr[i-1]-arr[j]
                j += 1
        return max(sizes)

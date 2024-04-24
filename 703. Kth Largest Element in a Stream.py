"""
114 ms runtime beats 13.26%
20.46 MB memory beats 72.69%
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        ln = len(nums)
        if not nums:
            self.hp = nums
        else:
            for i in range(ln//2-1, -1, -1):
                self.heapify_max(nums, ln, i)
            for i in range(ln-1, ln-k-1, -1):
                nums[0], nums[i] = nums[i], nums[0]
                self.heapify_max(nums, i, 0)
            self.hp = nums[-k:]

    def add(self, val: int) -> int:
        ln = len(self.hp)
        if ln<self.k:
            self.hp.append(val)
            ln += 1
            for i in range(ln//2-1, -1, -1):
                self.heapify_min(self.hp, ln, i)
            return self.hp[0]
        if val <= self.hp[0]:
            return self.hp[0]
        else:
            self.hp[0] = val
            self.heapify_min(self.hp, ln, 0)
            return self.hp[0]

    def heapify_min(self, arr, n, i):
        l = 2*i+1
        r = 2*i+2
        mi = i
        if l<n and arr[l]<arr[mi]:
            mi = l
        if r<n and arr[r]<arr[mi]:
            mi = r
        if mi != i:
            arr[mi], arr[i] = arr[i], arr[mi]
            return self.heapify_min(arr, n, mi)

    def heapify_max(self, arr, n, i):
        l = 2*i+1
        r = 2*i+2
        mx = i
        if l<n and arr[l]>arr[mx]:
            mx = l
        if r<n and arr[r]>arr[mx]:
            mx = r
        if mx != i:
            arr[mx], arr[i] = arr[i], arr[mx]
            return self.heapify_max(arr, n, mx)

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
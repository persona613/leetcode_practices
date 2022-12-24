"""
1601 ms runtime beats 31.17%
34.7 MB memory beats 16.31%
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def heapfy(heapsize, i):
            left = i*2+1
            right = i*2+2
            largest = i
            if left<heapsize and nums[left]>nums[largest]:
                largest = left
            if right<heapsize and nums[right]>nums[largest]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                return heapfy(heapsize, largest)
        
        for i in range(len(nums)//2-1, -1, -1):
            heapfy(len(nums), i)
            
        # even k=len(nums)=i=0, heapfy still ok
        for i in range(len(nums)-1, len(nums)-k-1, -1): 
            nums[0], nums[i] = nums[i], nums[0]
            heapfy(i, 0)
        print(nums)
        return nums[-k]
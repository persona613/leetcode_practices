"""
2449 ms runtime beats 62.39%
32.8 MB memory beats 5.86%
"""
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapfy(heapsize, i):
            left = i*2+1
            right = i*2+2
            largest = i
            if left < heapsize and nums[left]>nums[largest]:
                largest = left
            if right < heapsize and nums[right]>nums[largest]:
                largest = right
            if largest != i:
                nums[largest], nums[i] = nums[i], nums[largest]
                return heapfy(heapsize, largest)
        
        for i in range(len(nums)//2 - 1, -1, -1):
            heapfy(len(nums), i)
            
        for i in range(len(nums)-1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            heapfy(i , 0)
            
        return nums
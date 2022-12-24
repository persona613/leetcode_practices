'''
Runtime: 126 ms, faster than 75.89% of Python3 online submissions 
Memory Usage: 19.7 MB, less than 14.32% of Python3 online submissions
'''
# bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        
        for n, freq in count.items():
            bucket[freq].append(n) 
        flat = [n for bk in bucket for n in bk]
        
        return flat[::-1][:k]
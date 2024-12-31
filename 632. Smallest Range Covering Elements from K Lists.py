"""
191 ms runtime beats 65.73%
23.12 MB memory beats 79.95%
"""
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        # res range
        start, end = 0, float("inf")
        # min heap to track curr minim value, (value, row, col)
        q = []
        currmx = float("-inf")
        for i in range(m):
            heappush(q, (nums[i][0], i, 0))
            currmx = max(currmx, nums[i][0])
        
        while len(q) == m:
            currmi, row, col = heappop(q)
            if currmx - currmi < end - start:
                start = currmi
                end = currmx

            if col + 1 < len(nums[row]):
                nxt_value = nums[row][col + 1]
                heappush(q, (nxt_value, row, col + 1))
                currmx = max(currmx, nxt_value)
        return [start, end]
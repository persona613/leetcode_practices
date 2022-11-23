"""
Submission Result: Wrong Answer 
Input:
"dvdf"
Output:
2
Expected:
3
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        record = {}
        count = 0
        bag = set()
        if len(s) == 0:
            return 0
        for c in s:            
            if c in bag:
                record[count] = bag
                bag.clear()
                bag.add(c)
                count = 1
            else:
                bag.add(c)
                count += 1
        record[count] = bag
        return max(record.keys())    